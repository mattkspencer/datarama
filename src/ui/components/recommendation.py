import streamlit as st
from typing import Optional
from ...models import FinancialMetrics

def render_recommendation(metrics: Optional[FinancialMetrics], score: Optional[float] = None) -> None:
    """Render investment recommendation"""
    st.subheader("Investment Recommendation")
    
    if not metrics:
        st.error("Unable to generate investment recommendation due to insufficient data")
        st.write("This could be due to:")
        st.write("- Missing financial metrics")
        st.write("- Invalid or incomplete data from SEC")
        st.write("- API access issues")
        return
    
    if score is not None:
        if score >= 80:
            st.success("Strong Buy")
        elif score >= 60:
            st.info("Buy")
        elif score >= 40:
            st.warning("Hold")
        else:
            st.error("Sell")
        
        st.write(f"Investment Score: {score:.1f}/100")