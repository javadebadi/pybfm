"""Module for each item in balance sheet
"""

from .balance_sheet_main_group import (
    ASSET,
    EQUITY,
    LIABILITY,
    BalanceSheetMainGroup,
    )
from .balance_sheet_submain_group import (
    LONG_TERM_ASSET,
    LONG_TERM_LIABILITY,
    OWNERS_EQUITY,
    SHORT_TERM_ASSET,
    SHORT_TERM_LIABILITY,
    BalanceSheetSubMainGroup,
    )


class BalanceSheetItem:
    """Class to represent each balance sheet item in accounting.

    Each balance sheet item in accounting have the following properties:
        - account number: the unique IDentifier of this item
        - name: name of this aitem
        - origin: the origin of item of this item
        - balance sheet sub main group: each item must belong to a 
            a group in balance sheet
        - balance sheet main group: this property is readonly
        and is determined by balance sheet sub main group
    
    """

    def __init__(
        self,
        ID: str,
        name: str,
        origin: str = None,
        balance_sheet_sub_main_group: BalanceSheetSubMainGroup = None,
        ) -> None:
        self.ID = ID
        self.name = name
        self.origin = origin
        self.balance_sheet_sub_main_group = balance_sheet_sub_main_group

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        assert type(ID) == str or type(ID) == int
        self._ID = str(ID)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        assert type(name) == str
        self._name = name

    @property
    def balance_sheet_sub_main_group(self):
        return self._balance_sheet_sub_main_group

    @balance_sheet_sub_main_group.setter
    def balance_sheet_sub_main_group(self, balance_sheet_sub_main_group):
        assert isinstance(
            balance_sheet_sub_main_group,
            BalanceSheetSubMainGroup,
            )
        self._balance_sheet_sub_main_group = balance_sheet_sub_main_group

    @property
    def balance_sheet_main_group(self):
        return self._balance_sheet_sub_main_group.balance_sheet_main_group

    def __str__(self):
        return str(self.ID) + ' - ' + self.name

    def to_csv(self, depth: int = 0, end: str = "\n"):
        assert type(end) == str
        csv = f"{self.ID},{self.name},{self.origin},"\
              f"{self.balance_sheet_sub_main_group.to_csv(depth=depth-1)}"\
              + end
        return csv

    def is_main_asset(self):
        return self.balance_sheet_main_group == ASSET

    def is_main_liability(self):
        return self.balance_sheet_main_group == LIABILITY

    def is_main_equity(self):
        return self.balance_sheet_main_group == EQUITY

    def is_short_term_asset(self):
        return self.balance_sheet_sub_main_group == SHORT_TERM_ASSET

    def is_long_term_asset(self):
        return self.balance_sheet_sub_main_group == LONG_TERM_ASSET

    def is_short_term_liability(self):
        return self.balance_sheet_sub_main_group == SHORT_TERM_LIABILITY

    def is_long_term_liability(self):
        return self.balance_sheet_sub_main_group == LONG_TERM_LIABILITY

    def is_equity(self):
        return self.balance_sheet_sub_main_group == OWNERS_EQUITY
