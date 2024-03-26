# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_cleemy_expenses_python_sdk.paths.api_v3_expense_claims_creation.post import CreateNewExpenseClaimRaw
from lucca_cleemy_expenses_python_sdk.paths.api_v3_expense_claims.get import ListRaw


class ExpenseClaimsApiRaw(
    CreateNewExpenseClaimRaw,
    ListRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
