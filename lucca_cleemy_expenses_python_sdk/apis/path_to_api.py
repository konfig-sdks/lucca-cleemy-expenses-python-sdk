import typing_extensions

from lucca_cleemy_expenses_python_sdk.paths import PathValues
from lucca_cleemy_expenses_python_sdk.apis.paths.api_v3_expense_temp_items import ApiV3ExpenseTempItems
from lucca_cleemy_expenses_python_sdk.apis.paths.api_v3_expense_temp_items_expense_temp_item_id import ApiV3ExpenseTempItemsExpenseTempItemId
from lucca_cleemy_expenses_python_sdk.apis.paths.api_v3_expense_claims_creation import ApiV3ExpenseClaimsCreation
from lucca_cleemy_expenses_python_sdk.apis.paths.api_v3_expense_claims import ApiV3ExpenseClaims

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V3_EXPENSE_TEMP_ITEMS: ApiV3ExpenseTempItems,
        PathValues.API_V3_EXPENSE_TEMP_ITEMS_EXPENSE_TEMP_ITEM_ID: ApiV3ExpenseTempItemsExpenseTempItemId,
        PathValues.API_V3_EXPENSE_CLAIMS_CREATION: ApiV3ExpenseClaimsCreation,
        PathValues.API_V3_EXPENSE_CLAIMS: ApiV3ExpenseClaims,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V3_EXPENSE_TEMP_ITEMS: ApiV3ExpenseTempItems,
        PathValues.API_V3_EXPENSE_TEMP_ITEMS_EXPENSE_TEMP_ITEM_ID: ApiV3ExpenseTempItemsExpenseTempItemId,
        PathValues.API_V3_EXPENSE_CLAIMS_CREATION: ApiV3ExpenseClaimsCreation,
        PathValues.API_V3_EXPENSE_CLAIMS: ApiV3ExpenseClaims,
    }
)
