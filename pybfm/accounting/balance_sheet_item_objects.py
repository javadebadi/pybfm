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

ALLOWANCE_FOR_BAD_DEBTS = BalanceSheetItem(
    '101-0000000003',
    'Allowance for Bad Debts',
    'An allowance for bad debt is a valuation account used to estimate the amount of a firm\'s receivables that may ultimately be uncollectible.',
    SHORT_TERM_ASSET,
)

INVENTORY = BalanceSheetItem(
    '101-0000000004',
    'Inventory',
    'Inventory is the raw materials used to produce goods as well as the goods that are available for sale. The three types of inventory include raw materials, work-in-progress, and finished goods.',
    SHORT_TERM_ASSET,
)


SHORT_PREPAID_INSURANCE = BalanceSheetItem(
    '101-0000000005',
    'Prepaid Insurance',
    'A prepaid expense is carried on an insurance company\'s balance sheet as a current asset until it is consumed.',
    SHORT_TERM_ASSET,
)
