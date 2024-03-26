# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_cleemy_expenses_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V3_EXPENSE_TEMP_ITEMS = "/api/v3/expenseTempItems"
    API_V3_EXPENSE_TEMP_ITEMS_EXPENSE_TEMP_ITEM_ID = "/api/v3/expenseTempItems/{expenseTempItemId}"
    API_V3_EXPENSE_CLAIMS_CREATION = "/api/v3/expenseClaims/creation"
    API_V3_EXPENSE_CLAIMS = "/api/v3/expenseClaims"
