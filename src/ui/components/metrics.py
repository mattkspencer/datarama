import streamlit as st
from typing import Optional
from ...models import FinancialMetrics

def render_key_metrics(metrics: Optional[FinancialMetrics]) -> None:
    """Render key financial metrics"""
    st.subheader("Key Metrics")
    if metrics:
        st.write("Financial Data:")
        st.json({
            'Net Income': f"${metrics.net_income:,.2f}" if metrics.net_income else "N/A",
            'Shareholder Equity': f"${metrics.shareholder_equity:,.2f}" if metrics.shareholder_equity else "N/A",
            'Total Debt': f"${metrics.total_debt:,.2f}" if metrics.total_debt else "N/A",
            'Operating Cash Flow': f"${metrics.operating_cash_flow:,.2f}" if metrics.operating_cash_flow else "N/A",
            'Capital Expenditures': f"${metrics.capital_expenditures:,.2f}" if metrics.capital_expenditures else "N/A"
        })
    else:
        st.error("No metrics available")