import requests
import logging
from typing import Optional, Dict
from datetime import datetime
from src.models import FinancialMetrics

# Set up logging with more verbose output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ValueInvestingEngine:
    """Engine for fetching and analyzing financial data"""
    
    def __init__(self, email: str):
        """Initialize the Value Investing Engine."""
        self.sec_base_url = "https://data.sec.gov/api/xbrl/companyfacts/CIK"
        self.headers = {
            'User-Agent': f'Value Investing Tool ({email})',
            'Accept': 'application/json',
            'Host': 'data.sec.gov'
        }
        self.ticker_to_cik = {
            'AAPL': '0000320193',
            'MSFT': '0000789019',
            'GOOGL': '0001652044',
            'AMZN': '0001018724',
            'META': '0001326801',
            'NVDA': '0001045810',
            'TSLA': '0001318605'
        }
        print(f"Initialized with headers: {self.headers}")

    def get_financial_metrics(self, ticker: str) -> Optional[FinancialMetrics]:
        """Fetch financial metrics from SEC API"""
        try:
            print(f"\nFetching metrics for {ticker}")
            
            # Get CIK
            if ticker not in self.ticker_to_cik:
                print(f"Unsupported ticker: {ticker}")
                return None
                
            cik = self.ticker_to_cik[ticker]
            padded_cik = cik.zfill(10)
            url = f"{self.sec_base_url}{padded_cik}.json"
            
            print(f"Making request to: {url}")
            print(f"Using headers: {self.headers}")
            
            response = requests.get(url, headers=self.headers)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Error response: {response.status_code}")
                print(f"Response text: {response.text}")
                return None
            
            data = response.json()
            print(f"Response keys: {list(data.keys())}")
            
            facts = data.get('facts', {})
            print(f"Facts keys: {list(facts.keys())}")
            
            us_gaap = facts.get('us-gaap', {})
            print(f"us-gaap keys: {list(us_gaap.keys())}")
            
            print(f"Found {len(us_gaap)} metrics")
            
            # Initialize metrics dictionary
            metrics = {
                'net_income': None,
                'shareholder_equity': None,
                'total_debt': None,
                'operating_cash_flow': None,
                'capital_expenditures': None
            }
            
            # Extract metrics
            if 'NetIncomeLoss' in us_gaap:
                metrics['net_income'] = self.get_latest_value(us_gaap['NetIncomeLoss'])
                print(f"Net Income: {metrics['net_income']}")
            
            if 'StockholdersEquity' in us_gaap:
                metrics['shareholder_equity'] = self.get_latest_value(us_gaap['StockholdersEquity'])
                print(f"Equity: {metrics['shareholder_equity']}")
            
            if 'LongTermDebt' in us_gaap:
                metrics['total_debt'] = self.get_latest_value(us_gaap['LongTermDebt'])
                print(f"Debt: {metrics['total_debt']}")
            
            if 'NetCashProvidedByUsedInOperatingActivities' in us_gaap:
                metrics['operating_cash_flow'] = self.get_latest_value(us_gaap['NetCashProvidedByUsedInOperatingActivities'])
                print(f"Cash Flow: {metrics['operating_cash_flow']}")
            
            if 'CapitalExpenditures' in us_gaap:
                metrics['capital_expenditures'] = self.get_latest_value(us_gaap['CapitalExpenditures'])
                print(f"Capital Expenditures: {metrics['capital_expenditures']}")
            
            print(f"Final metrics: {metrics}")
            
            return FinancialMetrics(**metrics)
        except Exception as e:
            print(f"Error fetching financial metrics: {e}")
            return None

    def get_latest_value(self, data: dict) -> Optional[float]:
        """Extract the most recent value from SEC data"""
        try:
            if not data or 'units' not in data:
                return None
            
            values = data.get('units', {}).get('USD', [])
            if not values:
                return None
            
            # Sort by end date and get most recent value
            sorted_values = sorted(
                [v for v in values if 'end' in v and 'val' in v],
                key=lambda x: x['end'],
                reverse=True
            )
            
            if not sorted_values:
                return None
                
            return float(sorted_values[0]['val'])
            
        except Exception as e:
            print(f"Error getting latest value: {str(e)}")
            return None