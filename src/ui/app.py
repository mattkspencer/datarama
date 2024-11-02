import streamlit as st
from typing import Optional
from src.models import FinancialMetrics
from src.value_investing_engine import ValueInvestingEngine

class ValueInvestingApp:
    def run(self):
        """Run the Streamlit application"""
        st.title("Value Investing Analysis Tool")
        
        if 'engine' not in st.session_state:
            email = st.text_input(
                "Enter your email for SEC API access:",
                type="password",
                key="sec_email_input"
            )
            
            if email:
                st.session_state.engine = ValueInvestingEngine(email)
            else:
                st.warning("Please enter your email to access the SEC API")
                return
        
        # Show supported tickers
        st.write("📈 Supported Companies")
        st.write("Currently supporting major companies including:")
        for ticker in st.session_state.engine.ticker_to_cik.keys():
            st.write(f"- {ticker}")
        
        # Get user input
        ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()
        
        if st.button("Analyze", type="primary"):
            with st.spinner(f"Analyzing {ticker}..."):
                try:
                    metrics = st.session_state.engine.get_financial_metrics(ticker)
                    
                    if metrics:
                        st.success("Analysis Complete!")
                        st.write("Financial Metrics:")
                        st.json({
                            'Net Income': metrics.net_income,
                            'Shareholder Equity': metrics.shareholder_equity,
                            'Total Debt': metrics.total_debt,
                            'Operating Cash Flow': metrics.operating_cash_flow,
                            'Capital Expenditures': metrics.capital_expenditures
                        })
                    else:
                        st.error("Unable to fetch metrics")
                        
                except Exception as e:
                    st.error(f"Error analyzing {ticker}: {str(e)}")