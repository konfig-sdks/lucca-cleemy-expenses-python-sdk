<div align="left">

[![Visit Lucca](./header.png)](https://lucca-hr.com)

# Lucca<a id="lucca"></a>

Welcome on the documentation for the CleemyExpenses API.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`luccacleemyexpenses.expense_claims.create_new_expense_claim`](#luccacleemyexpensesexpense_claimscreate_new_expense_claim)
  * [`luccacleemyexpenses.expense_claims.list`](#luccacleemyexpensesexpense_claimslist)
  * [`luccacleemyexpenses.expenses.create_new_temporary_expense`](#luccacleemyexpensesexpensescreate_new_temporary_expense)
  * [`luccacleemyexpenses.expenses.get_by_id`](#luccacleemyexpensesexpensesget_by_id)
  * [`luccacleemyexpenses.expenses.list_temp_items`](#luccacleemyexpensesexpenseslist_temp_items)
  * [`luccacleemyexpenses.expenses.update_expense_temp_item`](#luccacleemyexpensesexpensesupdate_expense_temp_item)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lucca&serviceName=Cleemy%20Expenses&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lucca_cleemy_expenses_python_sdk import LuccaCleemyExpenses, ApiException

luccacleemyexpenses = LuccaCleemyExpenses(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new ExpenseClaim
    create_new_expense_claim_response = (
        luccacleemyexpenses.expense_claims.create_new_expense_claim(
            body=[
                {
                    "title": "title_example",
                    "expense_temp_items": [
                        {
                            "id": 1,
                        }
                    ],
                }
            ],
        )
    )
    print(create_new_expense_claim_response)
except ApiException as e:
    print("Exception when calling ExpenseClaimsApi.create_new_expense_claim: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["status"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from lucca_cleemy_expenses_python_sdk import LuccaCleemyExpenses, ApiException

luccacleemyexpenses = LuccaCleemyExpenses(
    authorization="YOUR_API_KEY",
)


async def main():
    try:
        # Create a new ExpenseClaim
        create_new_expense_claim_response = (
            await luccacleemyexpenses.expense_claims.acreate_new_expense_claim(
                body=[
                    {
                        "title": "title_example",
                        "expense_temp_items": [
                            {
                                "id": 1,
                            }
                        ],
                    }
                ],
            )
        )
        print(create_new_expense_claim_response)
    except ApiException as e:
        print(
            "Exception when calling ExpenseClaimsApi.create_new_expense_claim: %s\n" % e
        )
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["status"])
            pprint(e.body["message"])
        if e.status == 401:
            pprint(e.body["status"])
            pprint(e.body["message"])
        if e.status == 500:
            pprint(e.body["status"])
            pprint(e.body["message"])
        if e.status == 403:
            pprint(e.body["status"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lucca_cleemy_expenses_python_sdk import LuccaCleemyExpenses, ApiException

luccacleemyexpenses = LuccaCleemyExpenses(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new ExpenseClaim
    create_new_expense_claim_response = (
        luccacleemyexpenses.expense_claims.raw.create_new_expense_claim(
            body=[
                {
                    "title": "title_example",
                    "expense_temp_items": [
                        {
                            "id": 1,
                        }
                    ],
                }
            ],
        )
    )
    pprint(create_new_expense_claim_response.body)
    pprint(create_new_expense_claim_response.body["data"])
    pprint(create_new_expense_claim_response.headers)
    pprint(create_new_expense_claim_response.status)
    pprint(create_new_expense_claim_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ExpenseClaimsApi.create_new_expense_claim: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["status"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["status"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `luccacleemyexpenses.expense_claims.create_new_expense_claim`<a id="luccacleemyexpensesexpense_claimscreate_new_expense_claim"></a>

When a user wants to declare his expenses, he creates an `ExpenseClaim`.

An `ExpenseClaim` is created by regrouping one or more `ExpenseTempItems` and converting them into ExpenseClaimItems.

Once created, an `ExpenseClaim` has to be approved by his manager.

Multiple `ExpenseClaims` can be created through a single request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_expense_claim_response = (
    luccacleemyexpenses.expense_claims.create_new_expense_claim(
        body=[
            {
                "title": "title_example",
                "expense_temp_items": [
                    {
                        "id": 1,
                    }
                ],
            }
        ],
    )
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseClaimsCreateNewExpenseClaimRequest`](./lucca_cleemy_expenses_python_sdk/type/expense_claims_create_new_expense_claim_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseClaimsCreateNewExpenseClaimResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expense_claims_create_new_expense_claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseClaims/creation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccacleemyexpenses.expense_claims.list`<a id="luccacleemyexpensesexpense_claimslist"></a>

Retrieve a list of `ExpenseClaims`.

The `declaredOn` query parameter can operate comparisons with a given date-time value:
- `?declaredOn=2021-01-01`: strict equality.
- `?declaredOn=since,2021-01-01`: greater than or equal.
- `?declaredOn=until,2021-01-01`: lower than or equal.
- `?declaredOn=between,2021-01-01,2021-01-31`: comprised between two dates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = luccacleemyexpenses.expense_claims.list(
    paging="100,0",
    owner_id=[1],
    order_by="string_example",
    declared_on="string_example",
    status_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### paging: `str`<a id="paging-str"></a>

{offset},{limit}. Defaults to 0,1000.

##### owner_id: List[`int`]<a id="owner_id-listint"></a>

Comma-separated list of user identifiers (int).

##### order_by: `str`<a id="order_by-str"></a>

{fieldName},{'asc'||'desc'}. Example: `?orderby=declaredOn,desc`

##### declared_on: `str`<a id="declared_on-str"></a>

Examples: `between,2022-01-01,202201-31`.

##### status_id: `str`<a id="status_id-str"></a>

1: Created; 2: PartiallyApproved; 3: Approved; 4: Controlled; 5: ApprovedAndControlled; 6: PaymentInitiated; 7: Paid; 8: Refused; 9: Cancelled. Examples: `2,3` or `PartiallyApproved,Approved`.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseClaimsListResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expense_claims_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseClaims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccacleemyexpenses.expenses.create_new_temporary_expense`<a id="luccacleemyexpensesexpensescreate_new_temporary_expense"></a>

Create a new temporary expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_temporary_expense_response = (
    luccacleemyexpenses.expenses.create_new_temporary_expense(
        purchased_on="1970-01-01T00:00:00.00Z",
        expense_nature_id=1,
        id=11022,
        original_transaction={
            "gross_amount": 45.26,
            "currency_id": "GBP",
            "is_expense_abroad": False,
        },
        processed_amounts={
            "gross_amount": 57.9,
            "currency_id": "GBP",
            "net_amount": 57.9,
        },
        mileage=None,
        quantity=1,
        effective_quantity=3,
        attendees=None,
        axis_sections=[None],
        custom_fields={
            "key": {},
        },
        merchant=None,
        comment=None,
        expense_receipts=[{}],
        authorized_actions={
            "is_cancellable": True,
            "is_editable": True,
        },
        source_id={},
        source={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
        owner_id=361,
        payment_method_id=0,
        payment_method={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
        status_id={
            "id": 0,
        },
        status={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### purchased_on: `datetime`<a id="purchased_on-datetime"></a>

Day the expense was made.

##### expense_nature_id: `int`<a id="expense_nature_id-int"></a>

Nature of the expense: Meals, Train, Taxi, Hotels, Taxi, Mileage... List depends on the app configuration.

##### id: `int`<a id="id-int"></a>

##### original_transaction: [`ExpenseTempItemOriginalTransaction`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_original_transaction.py)<a id="original_transaction-expensetempitemoriginaltransactionlucca_cleemy_expenses_python_sdktypeexpense_temp_item_original_transactionpy"></a>


##### processed_amounts: [`ExpenseTempItemProcessedAmounts`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_processed_amounts.py)<a id="processed_amounts-expensetempitemprocessedamountslucca_cleemy_expenses_python_sdktypeexpense_temp_item_processed_amountspy"></a>


##### mileage: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="mileage-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Additional information when the expense type is mileage.

##### quantity: `int`<a id="quantity-int"></a>

The quantity when the expense type is 'Quantity'.

##### effective_quantity: `int`<a id="effective_quantity-int"></a>

Calculated quantity when the expense type is 'Quantity' or 'Invitations' (number of attendees).

##### attendees: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="attendees-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Additional information when the expense type is 'Invitation'.

##### axis_sections: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="axis_sections-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Axis sections values.

##### custom_fields: [`Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`](./lucca_cleemy_expenses_python_sdk/type/typing_dict_str_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="custom_fields-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_dict_str_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Values for custom fields.

##### merchant: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="merchant-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Merchant of the expense.

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### expense_receipts: List[`ExpenseReceipt`]<a id="expense_receipts-listexpensereceipt"></a>

The original receipt (PDF file, image, ...).

##### authorized_actions: [`ExpenseTempItemAuthorizedActions`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_authorized_actions.py)<a id="authorized_actions-expensetempitemauthorizedactionslucca_cleemy_expenses_python_sdktypeexpense_temp_item_authorized_actionspy"></a>


##### source_id: [`SourceId`](./lucca_cleemy_expenses_python_sdk/type/source_id.py)<a id="source_id-sourceidlucca_cleemy_expenses_python_sdktypesource_idpy"></a>


##### source: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="source-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


##### owner_id: `int`<a id="owner_id-int"></a>

Unique identifier of the user that made this expense.

##### payment_method_id: [`PaymentMethodId`](./lucca_cleemy_expenses_python_sdk/type/payment_method_id.py)<a id="payment_method_id-paymentmethodidlucca_cleemy_expenses_python_sdktypepayment_method_idpy"></a>

##### payment_method: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="payment_method-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


##### status_id: [`StatusId`](./lucca_cleemy_expenses_python_sdk/type/status_id.py)<a id="status_id-statusidlucca_cleemy_expenses_python_sdktypestatus_idpy"></a>


##### status: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="status-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseTempItem`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpensesCreateNewTemporaryExpenseResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expenses_create_new_temporary_expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseTempItems` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccacleemyexpenses.expenses.get_by_id`<a id="luccacleemyexpensesexpensesget_by_id"></a>

Get an ExpenseTempItem by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = luccacleemyexpenses.expenses.get_by_id(
    expense_temp_item_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_temp_item_id: `int`<a id="expense_temp_item_id-int"></a>

Unique identifier of the ExpenseTempItem.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpensesGetByIdResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expenses_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseTempItems/{expenseTempItemId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccacleemyexpenses.expenses.list_temp_items`<a id="luccacleemyexpensesexpenseslist_temp_items"></a>

Retrieve a list of `ExpenseTempItems`.

The `purchasedOn` query parameter can operate comparisons with a given date-time value:
- `?purchasedOn=2021-01-01`: strict equality.
- `?purchasedOn=since,2021-01-01`: greater than or equal.
- `?purchasedOn=until,2021-01-01`: lower than or equal.
- `?purchasedOn=between,2021-01-01,2021-01-31`: comprised between two dates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_temp_items_response = luccacleemyexpenses.expenses.list_temp_items(
    paging="100,0",
    owner_id=[None],
    order_by="string_example",
    purchased_on="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### paging: `str`<a id="paging-str"></a>

{offset},{limit}. Defaults to 0,1000.

##### owner_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="owner_id-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Comma-separated list of user identifiers (int).

##### order_by: `str`<a id="order_by-str"></a>

{fieldName},{'asc'||'desc'}. Example: `?orderby=purchasedOn,desc`

##### purchased_on: `str`<a id="purchased_on-str"></a>

Examples: `between,2022-01-01,202201-31`.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpensesListTempItemsResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expenses_list_temp_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseTempItems` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccacleemyexpenses.expenses.update_expense_temp_item`<a id="luccacleemyexpensesexpensesupdate_expense_temp_item"></a>

Update an ExpenseTempItem by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_expense_temp_item_response = (
    luccacleemyexpenses.expenses.update_expense_temp_item(
        purchased_on="1970-01-01T00:00:00.00Z",
        expense_nature_id=1,
        expense_temp_item_id=1,
        id=11022,
        original_transaction={
            "gross_amount": 45.26,
            "currency_id": "GBP",
            "is_expense_abroad": False,
        },
        processed_amounts={
            "gross_amount": 57.9,
            "currency_id": "GBP",
            "net_amount": 57.9,
        },
        mileage=None,
        quantity=1,
        effective_quantity=3,
        attendees=None,
        axis_sections=[None],
        custom_fields={
            "key": {},
        },
        merchant=None,
        comment=None,
        expense_receipts=[{}],
        authorized_actions={
            "is_cancellable": True,
            "is_editable": True,
        },
        source_id={},
        source={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
        owner_id=361,
        payment_method_id=0,
        payment_method={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
        status_id={
            "id": 0,
        },
        status={
            "id": 6,
            "name": "API",
            "code": "Api",
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### purchased_on: `datetime`<a id="purchased_on-datetime"></a>

Day the expense was made.

##### expense_nature_id: `int`<a id="expense_nature_id-int"></a>

Nature of the expense: Meals, Train, Taxi, Hotels, Taxi, Mileage... List depends on the app configuration.

##### expense_temp_item_id: `int`<a id="expense_temp_item_id-int"></a>

Unique identifier of the ExpenseTempItem.

##### id: `int`<a id="id-int"></a>

##### original_transaction: [`ExpenseTempItemOriginalTransaction`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_original_transaction.py)<a id="original_transaction-expensetempitemoriginaltransactionlucca_cleemy_expenses_python_sdktypeexpense_temp_item_original_transactionpy"></a>


##### processed_amounts: [`ExpenseTempItemProcessedAmounts`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_processed_amounts.py)<a id="processed_amounts-expensetempitemprocessedamountslucca_cleemy_expenses_python_sdktypeexpense_temp_item_processed_amountspy"></a>


##### mileage: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="mileage-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Additional information when the expense type is mileage.

##### quantity: `int`<a id="quantity-int"></a>

The quantity when the expense type is 'Quantity'.

##### effective_quantity: `int`<a id="effective_quantity-int"></a>

Calculated quantity when the expense type is 'Quantity' or 'Invitations' (number of attendees).

##### attendees: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="attendees-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Additional information when the expense type is 'Invitation'.

##### axis_sections: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="axis_sections-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Axis sections values.

##### custom_fields: [`Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`](./lucca_cleemy_expenses_python_sdk/type/typing_dict_str_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="custom_fields-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_dict_str_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Values for custom fields.

##### merchant: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="merchant-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Merchant of the expense.

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_cleemy_expenses_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_cleemy_expenses_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### expense_receipts: List[`ExpenseReceipt`]<a id="expense_receipts-listexpensereceipt"></a>

The original receipt (PDF file, image, ...).

##### authorized_actions: [`ExpenseTempItemAuthorizedActions`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item_authorized_actions.py)<a id="authorized_actions-expensetempitemauthorizedactionslucca_cleemy_expenses_python_sdktypeexpense_temp_item_authorized_actionspy"></a>


##### source_id: [`SourceId`](./lucca_cleemy_expenses_python_sdk/type/source_id.py)<a id="source_id-sourceidlucca_cleemy_expenses_python_sdktypesource_idpy"></a>


##### source: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="source-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


##### owner_id: `int`<a id="owner_id-int"></a>

Unique identifier of the user that made this expense.

##### payment_method_id: [`PaymentMethodId`](./lucca_cleemy_expenses_python_sdk/type/payment_method_id.py)<a id="payment_method_id-paymentmethodidlucca_cleemy_expenses_python_sdktypepayment_method_idpy"></a>

##### payment_method: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="payment_method-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


##### status_id: [`StatusId`](./lucca_cleemy_expenses_python_sdk/type/status_id.py)<a id="status_id-statusidlucca_cleemy_expenses_python_sdktypestatus_idpy"></a>


##### status: [`Enum`](./lucca_cleemy_expenses_python_sdk/type/enum.py)<a id="status-enumlucca_cleemy_expenses_python_sdktypeenumpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseTempItem`](./lucca_cleemy_expenses_python_sdk/type/expense_temp_item.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpensesUpdateExpenseTempItemResponse`](./lucca_cleemy_expenses_python_sdk/pydantic/expenses_update_expense_temp_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/expenseTempItems/{expenseTempItemId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
