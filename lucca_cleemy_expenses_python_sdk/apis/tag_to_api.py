import typing_extensions

from lucca_cleemy_expenses_python_sdk.apis.tags import TagValues
from lucca_cleemy_expenses_python_sdk.apis.tags.expenses_api import ExpensesApi
from lucca_cleemy_expenses_python_sdk.apis.tags.expense_claims_api import ExpenseClaimsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EXPENSES: ExpensesApi,
        TagValues.EXPENSE_CLAIMS: ExpenseClaimsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EXPENSES: ExpensesApi,
        TagValues.EXPENSE_CLAIMS: ExpenseClaimsApi,
    }
)
