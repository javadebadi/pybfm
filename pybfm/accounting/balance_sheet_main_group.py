"""
Module for main group of items in Balance Sheet.

There are Three main groups in a balance sheet:

    - Asset
    - Liability
    - Equity
"""


class BalanceSheetMainGroup:
    """
    Class to determine Balance Sheet Group.

    Balance Sheet Main Group is one the followings:
    - Asset
    - Liability
    - Equity

    Example
    -------
    ASSET = BalanceSheetMainGroup(id=1, name="Asset")
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
        """Returns a string which can be used to generated csv files.

        Parameters
        ----------
        depth : int
            If non-negative will return information of BalanceSheetMainGroup 
            object as string. Else, empty string will be returned.
        end : str
            Determines the string to append at the end of the 

        
        Example
        -------
        >> bsmg = BalanceSheetMainGroup(id=1, name="Asset")
        >>> bsmg.to_csv()
        '1,Asset'
        >>> bsmg.to_csv(-1)
        ''
        >>> bsmg.to_csv(end="\n")
        >>>
        '1,Asset
        '
        """
        assert type(depth) == int
        if depth < 0:
            return "" + end
        else:
            return f"{self.id},{self.name}" + end

    def __eq__(self, other) -> bool:
        return self.id == other.id


# Balance Sheet Main Group Objects
ASSET = BalanceSheetMainGroup(
    id=1,
    name='Asset',
    )
LIABILITY = BalanceSheetMainGroup(
    id=2,
    name='Liability',
    )
EQUITY = BalanceSheetMainGroup(
    id=3,
    name='Equity',
    )

BALANCE_SHEET_MAIN_GROUP_OBJECTS = [
    ASSET,
    LIABILITY,
    EQUITY,
]


class BalanceSheetMainGroupObjects:

    """Class with class level attributes which contains
    standard balance sheet main group objects.

    Attributes
    ----------
    ASSET : BalanceSheetMainGroup
    LIABILITY : BalanceSheetMainGroup
    EQUITY : BalanceSheetMainGroup
    """

    ASSET = ASSET
    LIABILITY = LIABILITY
    EQUITY = EQUITY