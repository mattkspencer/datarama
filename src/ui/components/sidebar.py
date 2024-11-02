import streamlit as st
from typing import Dict, Any

def render_sidebar() -> Dict[str, Any]:
    """Render sidebar inputs"""
    st.sidebar.header("Analysis Parameters")
    
    ticker = st.sidebar.text_input(
        "Enter Stock Ticker:",
        value="AAPL"
    ).upper()
    
    growth_rate = st.sidebar.slider(
        "Growth Rate (%)",
        min_value=0,
        max_value=20,
        value=10
    )
    
    discount_rate = st.sidebar.slider(
        "Discount Rate (%)",
        min_value=5,
        max_value=20,
        value=10
    )
    
    return {
        "ticker": ticker,
        "growth_rate": growth_rate,
        "discount_rate": discount_rate
    } 