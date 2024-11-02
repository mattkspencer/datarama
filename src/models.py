from dataclasses import dataclass
from typing import Optional

@dataclass
class FinancialMetrics:
    """Financial metrics data class"""
    net_income: Optional[float] = None
    shareholder_equity: Optional[float] = None
    total_debt: Optional[float] = None
    operating_cash_flow: Optional[float] = None
    capital_expenditures: Optional[float] = None

    def __init__(self, **kwargs):
        """Initialize with optional kwargs"""
        self.net_income = kwargs.get('net_income')
        self.shareholder_equity = kwargs.get('shareholder_equity')
        self.total_debt = kwargs.get('total_debt')
        self.operating_cash_flow = kwargs.get('operating_cash_flow')
        self.capital_expenditures = kwargs.get('capital_expenditures')

    def __str__(self):
        """String representation of metrics"""
        return (
            f"FinancialMetrics("
            f"net_income={self.net_income}, "
            f"shareholder_equity={self.shareholder_equity}, "
            f"total_debt={self.total_debt}, "
            f"operating_cash_flow={self.operating_cash_flow}, "
            f"capital_expenditures={self.capital_expenditures})"
        )

@dataclass
class Analysis:
    roe: Optional[float]
    debt_to_equity: Optional[float]
    free_cash_flow: Optional[float]
    intrinsic_value: Optional[float]
    investment_score: Optional[float] 