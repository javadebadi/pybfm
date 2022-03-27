from unittest import TestCase

from pybfm.accounting.balance_sheet_main_group import (
    BalanceSheetMainGroup,
    ASSET,
    LIABILITY,
    EQUITY,
    BALANCE_SHEET_MAIN_GROUP_OBJECTS,
    )
from pybfm.accounting.balance_sheet_submain_group import (
    BalanceSheetSubMainGroup,
    SHORT_TERM_ASSET,
    SHORT_TERM_LIABILITY,
    LONG_TERM_ASSET,
    LONG_TERM_LIABILITY,
    OWNERS_EQUITY,
)


class BalanceSheetSubMainGroupTest(TestCase):

    def test_balance_sheet_sub_main_group(self):
        b = BalanceSheetSubMainGroup(
            id=1,
            name='Short Term Asset',
            balance_sheet_main_group=ASSET,
            )
        self.assertEqual(b.name, 'Short Term Asset')
        self.assertEqual(b.id, 1)
        self.assertEqual(b.balance_sheet_main_group, ASSET)
        self.assertEqual(b.to_csv(depth=-1), '')
        self.assertEqual(b.to_csv(depth=0), '1,Short Term Asset')
        self.assertEqual(b.to_csv(depth=1), '1,Short Term Asset,1,Asset')
        self.assertEqual(b.to_csv(depth=2), '1,Short Term Asset,1,Asset')

class BalanceSheetSubMainGroupObjectsTest(TestCase):

    def test_object_SHORT_TERM_ASSET(self):
        self.assertEqual(SHORT_TERM_ASSET.id, 1)
        self.assertEqual(SHORT_TERM_ASSET.name, 'Short Term Asset')
        self.assertEqual(SHORT_TERM_ASSET.balance_sheet_main_group, ASSET)

    def test_object_LONG_TERM_ASSET(self):
        self.assertEqual(LONG_TERM_ASSET.id, 2)
        self.assertEqual(LONG_TERM_ASSET.name, 'Long Term Asset')
        self.assertEqual(LONG_TERM_ASSET.balance_sheet_main_group, ASSET)

    def test_object_SHORT_TERM_LIABILITY(self):
        self.assertEqual(SHORT_TERM_LIABILITY.id, 11)
        self.assertEqual(SHORT_TERM_LIABILITY.name, 'Short Term Liability')
        self.assertEqual(SHORT_TERM_LIABILITY.balance_sheet_main_group, LIABILITY)

    def test_object_LONG_TERM_LIABILITY(self):
        self.assertEqual(LONG_TERM_LIABILITY.id, 12)
        self.assertEqual(LONG_TERM_LIABILITY.name, 'Long Term Liability')
        self.assertEqual(LONG_TERM_LIABILITY.balance_sheet_main_group, LIABILITY)

    def test_object_OWNERS_EQUITY(self):
        self.assertEqual(OWNERS_EQUITY.id, 21)
        self.assertEqual(OWNERS_EQUITY.name, 'Owner\'s Equity')
        self.assertEqual(OWNERS_EQUITY.balance_sheet_main_group, EQUITY)

