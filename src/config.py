from typing import Dict
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# API Configuration
SEC_API_EMAIL = os.getenv('SEC_API_EMAIL')
SEC_BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK"

# Analysis Configuration
DEFAULT_GROWTH_RATE = 0.05
DEFAULT_DISCOUNT_RATE = 0.10
DEFAULT_PROJECTION_YEARS = 10

# Scoring Thresholds
ROE_THRESHOLDS = {
    'excellent': 15,
    'good': 10,
    'fair': 5
}

DEBT_EQUITY_THRESHOLDS = {
    'excellent': 0.5,
    'good': 1.0,
    'fair': 2.0
}

# Scoring Weights
SCORE_WEIGHTS = {
    'roe': 0.4,
    'debt': 0.3,
    'cash_flow': 0.3
}

# Add these constants
DEFAULT_TICKER = "AAPL"
CACHE_TTL = 3600  # 1 hour cache for analysis results

# UI Configuration
DEFAULT_TICKER = "AAPL"
CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))

# SEC API Configuration
SEC_RATE_LIMIT_DELAY = 0.1  # seconds between requests
SEC_MAX_RETRIES = 3
SEC_BACKOFF_FACTOR = 1
SEC_TIMEOUT = 10

# Logging Configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Cache Configuration
CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))  # 1 hour default
CACHE_MAX_ITEMS = 1000

def get_sec_headers(email: str) -> Dict[str, str]:
    """Get headers for SEC API requests"""
    return {
        'User-Agent': f'Value Investing Tool ({email})',
        'Accept': 'application/json',
        'Host': 'data.sec.gov'
    } 