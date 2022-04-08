"""Balance Sheet Items Objects
"""
from .balance_sheet_item import BalanceSheetItem
from .balance_sheet_submain_group import (
    SHORT_TERM_ASSET,
    LONG_TERM_ASSET,
    SHORT_TERM_LIABILITY,
    LONG_TERM_LIABILITY,
    OWNERS_EQUITY,
)

# Balance Sheet Item Objects
# These are objects that can be used 

CASH = BalanceSheetItem(
    '101-0000000001',
    'Cash',
    'Cash available',
    SHORT_TERM_ASSET,
)

ACCOUNTS_RECEIVABLE = BalanceSheetItem(
    '101-0000000002',
    'Accounts Receivable',
    'Accounts receivable (AR) is the balance of money due to a firm for goods or services delivered or used but not yet paid for by customer',
    SHORT_TERM_ASSET,
)