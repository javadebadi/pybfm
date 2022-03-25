"""Module for main group of items in Balance Sheet
"""
class BalanceSheetMainGroup:
    """
    Class to determine Balance Sheet Group.

    Balance Sheet Main Group is one the followings:
    - Asset
    - Liability
    - Equity

    """

    def __init__(
        self,
        id: int = None,
        name: str = None,
        ) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"BalanceSheetMainGroup(id={self.id}, name={self.name})"

    def to_csv(self, depth=0, end=""):
        assert type(depth) == int
        if depth <= 0:
            return f"{self.id},{self.name}" + end
        else:
            return f"{self.id},{self.name}" + end

    def __eq__(self, other) -> bool:
        return self.id == other.id


# Balance Sheet Main Group Objects
ASSET = BalanceSheetMainGroup(id=1, name='Asset')
LIABILITY = BalanceSheetMainGroup(id=2, name='Liability')
EQUITY = BalanceSheetMainGroup(id=3, name='Equity')

BALANCE_SHEET_MAIN_GROUP_OBJECTS = [
    ASSET,
    LIABILITY,
    EQUITY,
]