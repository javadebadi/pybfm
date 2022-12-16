"""Balance Sheet Items Objects
"""
from .balance_sheet_item import (
    BalanceSheetItem,
)
from .balance_sheet_submain_group import BalanceSheetSubMainGroupObjects as BSSubMain

# Balance Sheet Item Objects
# These are objects that can be used

CASH = BalanceSheetItem(
    "101-0000000001",
    "Cash",
    "Cash available",
    BSSubMain.SHORT_TERM_ASSET,
)

ACCOUNTS_RECEIVABLE = BalanceSheetItem(
    "101-0000000002",
    "Accounts Receivable",
    "Accounts receivable (AR) is the balance of money due to a firm for goods or services delivered or used but not yet paid for by customer",
    BSSubMain.SHORT_TERM_ASSET,
)

ALLOWANCE_FOR_BAD_DEBTS = BalanceSheetItem(
    "101-0000000003",
    "Allowance for Bad Debts",
    "An allowance for bad debt is a valuation account used to estimate the amount of a firm's receivables that may ultimately be uncollectible.",
    BSSubMain.SHORT_TERM_ASSET,
)

INVENTORY = BalanceSheetItem(
    "101-0000000004",
    "Inventory",
    "Inventory is the raw materials used to produce goods as well as the goods that are available for sale."
    "The three types of inventory include raw materials, work-in-progress, and finished goods.",
    BSSubMain.SHORT_TERM_ASSET,
)

SHORT_PREPAID_INSURANCE = BalanceSheetItem(
    "101-0000000005",
    "Prepaid Insurance",
    "A prepaid expense is carried on an insurance company's balance sheet as a current asset until it is consumed.",
    BSSubMain.SHORT_TERM_ASSET,
)

TRUCK = BalanceSheetItem(
    "102-0000000001",
    "Truck",
    "Trucks",
    BSSubMain.LONG_TERM_ASSET,
)

LAND = BalanceSheetItem(
    "102-0000000002",
    "Land",
    "Land",
    BSSubMain.LONG_TERM_ASSET,
)

BUILDING = BalanceSheetItem(
    "102-0000000003",
    "Building",
    "Building",
    BSSubMain.LONG_TERM_ASSET,
)

PREPAID_INSURANCE = BalanceSheetItem(
    "101-0000000004",
    "Prepaid Insurance",
    "A prepaid expense is carried on an insurance company's balance sheet as a current asset until it is consumed.",
    BSSubMain.LONG_TERM_ASSET,
)


ACCOUNTS_PAYABLE = BalanceSheetItem(
    "201-0000000001",
    "Accounts Payable",
    "Accounts Payable",
    BSSubMain.SHORT_TERM_LIABILITY,
)

NOTES_PAYABLE = BalanceSheetItem(
    "211-0000000001",
    "Notes Payable",
    "Notes Payable",
    BSSubMain.LONG_TERM_LIABILITY,
)

ORIGINAL_INVESTMENT = BalanceSheetItem(
    "211-0000000001",
    "Original Investment",
    "Original invesetment by owners of the company",
    BSSubMain.OWNERS_EQUITY,
)
RETAINED_EARNINGS = BalanceSheetItem(
    "211-0000000001",
    "Retained Earnings",
    "Retained Earnings is the earning that is re-invested in the company",
    BSSubMain.OWNERS_EQUITY,
)
