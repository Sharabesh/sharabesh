from typing import Dict
from itertools import islice
from .proforma import *
from .mortgage import Mortgage
import numpy as np


def _get_principle_paid_since(years, m: "Mortgage") -> float:
    return float(
        sum(month[0] for month in islice(m.monthly_payment_schedule(), 12 * years))
    )


def _get_principle_paid_between(year1, year2, m: "Mortgage") -> float:
    return float(
        sum(
            month[0]
            for month in islice(m.monthly_payment_schedule(), 12 * year1, 12 * year2)
        )
    )


def get_hard_costs():
    overhead = SITE_COSTS + BUILDING_CONSTRUCTION + MEPS
    return (1 + CONTIGENCY_PERCENTAGE) * (
        GENERAL_CONDITIONS_AND_OTHER + (1 + GC_OVERHEAD_PERCENTAGE) * overhead
    )


def get_due_diligence_costs():
    return (
        PHASE_1_ENV
        + PCA
        + ALTA_SURVEY
        + TRAVEL
        + PLATTING
        + PRELIM_SITE_PLAN
        + PRELIM_STORMW_STUDY
        + TRAFFIC_STUDIES
        + EASEMENTS
    )


def get_soft_costs():
    return (
        (1 + CONTINGENCY_PERCENTAGE_SOFT_COSTS) * TRANSFER_AND_RECORDATION_TAX
        + LEGAL_FEES
        + DUE_DILIGENCE
        + TITLE_INSURANCE
        + CONSTRUCTION_MANAGEMENT_PERCENTAGE * get_hard_costs()
        + MARKET_STUDY
        + ARCHITECTURAL
        + GEOTECH
        + CIVIL_END_LANDSCAPE_DESIGN
        + STRUCTURAL
        + MEP
        + MARKETING_PROMOTIONAL
        + BROKERAGE_FEES
        + IMPACT_FEES
        + LEGAL_CONSTRUCTION
        + LEGAL_LEASING
        + LEGAL_DEVELOPMENT
        + BUILDERS_RISK_INSURANCE
        + PROPERTY_TAXES_DURING_CONSTRUCTION
    )


def get_financing_costs() -> float:
    return (
        APPRAISAL
        + LEGAL_LOAN
        + LEGAL_PPM
        + POINTS_AND_FEES
        + WORKING_CAPITAL * (CONTIGENCY_PERCENTAGE_FINANCING + 1)
    )


def get_development_fee() -> float:
    return DEVELOPMENT_FEE_PERCENTAGE * (
        get_financing_costs() + get_soft_costs() + get_hard_costs() + ACQUISITION_COST
    )


def get_total_expenses():
    return (
        ACQUISITION_COST
        + get_hard_costs()
        + get_soft_costs()
        + get_financing_costs()
        + get_development_fee()
        + get_due_diligence_costs()
    )


def calculate_financing_assumptions(acquisition_cost, ltv_percentage) -> Dict[str, int]:
    total_cost = get_total_expenses()
    m = Mortgage(interest=INTEREST, amount=total_cost, months=12 * AMORTIZATION_YEARS)
    return {
        "Loan Amount": total_cost * ltv_percentage,
        "Equity Required": total_cost - (total_cost * ltv_percentage),
        "Annual Payment": float(m.monthly_payment()) * 12,
    }


def get_years_rent(year_number=0):
    gross_rent = GROSS_POTENTIAL_RENT
    while year_number > 0:
        gross_rent += gross_rent * YEAR_OVER_YEAR_RENT_INCREASE
        year_number -= 1
    return gross_rent


def get_fees_and_expenses(year_number=0):
    gross_rent = get_years_rent(year_number)
    effective_gross_income = gross_rent - (VACANCY_PERCENTAGE * gross_rent)
    property_management_fee = PROPERTY_MANAGEMENT_FEE * effective_gross_income
    return (
        ANNUAL_TAX_COST
        + ANNUAL_INSURANCE
        + RM_TURN_AND_CONT_SVCS
        + ADMIN_AND_MARKETING
        + UTILITIES
        + REPLACEMENT_RESERVES
        + PERSONNEL
        + property_management_fee
    )


def get_noi(year_number=0):
    gross_rent = get_years_rent(year_number)
    effective_gross_income = gross_rent - (VACANCY_PERCENTAGE * gross_rent)
    return effective_gross_income - get_fees_and_expenses(year_number)


def get_operating_cash_flow(year_number=0):
    years_noi = get_noi(year_number)
    equity_invested = calculate_financing_assumptions(ACQUISITION_COST, LTV_PERCENTAGE)[
        "Equity Required"
    ]
    annual_debt_payment = calculate_financing_assumptions(
        ACQUISITION_COST, LTV_PERCENTAGE
    )["Annual Payment"]
    asset_management_fee = ASSET_MANAGEMENT_FEE_PERCENTAGE * equity_invested
    return years_noi - annual_debt_payment - asset_management_fee


def get_sale_proceeds(year_number):
    """Calculates the cash out from equity at Year N"""
    total_cost = get_total_expenses()
    m = Mortgage(interest=INTEREST, amount=total_cost, months=12 * AMORTIZATION_YEARS)
    return _get_principle_paid_since(year_number, m)


def calculate_financial_ratios():
    assumptions = calculate_financing_assumptions(ACQUISITION_COST, LTV_PERCENTAGE)
    print("GOT ASSUMPTIONS")
    annual_payment = assumptions["Annual Payment"]
    loan_amount = assumptions["Loan Amount"]
    equity_invested = assumptions["Equity Required"]
    sum_of_cash_flows = sum(
        [get_operating_cash_flow(year) for year in range(HOLD_TERM_YEARS)]
    ) + get_sale_proceeds(HOLD_TERM_YEARS)
    print("Operating cash flows ", [get_operating_cash_flow(year) for year in range(HOLD_TERM_YEARS)])

    return {
        "Cap Rate": get_noi() / ACQUISITION_COST,
        "Year 1 Cash on Cash": get_noi() - annual_payment,
        "DSCR": -get_noi() / annual_payment,
        "Debt Yield": get_noi() / loan_amount,
        "Projected Equity Multiple": sum_of_cash_flows / equity_invested,
        "Projected IRR": np.irr(
            [get_operating_cash_flow(year) for year in range(HOLD_TERM_YEARS)]
        ),
    }
