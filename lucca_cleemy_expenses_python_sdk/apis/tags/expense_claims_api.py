# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_cleemy_expenses_python_sdk.paths.api_v3_expense_claims_creation.post import CreateNewExpenseClaim
from lucca_cleemy_expenses_python_sdk.paths.api_v3_expense_claims.get import List
from lucca_cleemy_expenses_python_sdk.apis.tags.expense_claims_api_raw import ExpenseClaimsApiRaw


class ExpenseClaimsApi(
    CreateNewExpenseClaim,
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ExpenseClaimsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ExpenseClaimsApiRaw(api_client)
