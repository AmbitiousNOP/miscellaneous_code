"""
Yahtzee game implementation by Conrad P
"""

from enum import Enum
from typing import Tuple, Union, Iterable


class Type(Enum):
    ACES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    THREE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 9
    SMALL_STRAIGHT = 10
    LARGE_STRAIGHT = 11
    YAHTZEE = 12
    CHANCE = 13


class Roll:
    def __init__(self, *args: Union[int, Iterable[int], Tuple]) -> None:
        """
        Initialize a roll object with 5 dice values.
        Args:
            *args: Either 5 ints, or an interable of 5 ints.
        Raises: 
            TypeError: If the input is not 5 ints or an interable of 5 ints.
        """
        # check if iterable
        if len(args) == 1 and isinstance(args[0], Iterable) and not isinstance(args[0], int):
            self.dice = tuple(args[0])
        # check if its ints past as args and convert to a tuple.
        elif len(args) == 5 and all(isinstance(arg, int) for arg in args):
            self.dice = tuple(args)
        else:
            raise TypeError(
                "Roll must be initialized with 5 integers or an iterable of 5 integers")

        if len(self.dice) != 5:
            raise TypeError("Roll must contain exactly 5 dice")

        if not all(isinstance(die, int) for die in self.dice):
            raise TypeError("All dice must be integers")

        self.counts = [self.dice.count(i) for i in range(1, 7)]

    def __eq__(self, other: object) -> bool:
        """
        Check if this roll is equal to another roll

        Args: 
            other: The object to compare with.

        Returns:
            bool: True if the rolls are equal, false otherwise. 
        """
        if not isinstance(other, Roll):
            return NotImplemented
        return sorted(self.dice) == sorted(other.dice)

    @property
    def aces(self) -> int:
        """
        Calculate the score for the Aces category

        Returns:
            int: the sum of all dice showing 1
        """
        return self.counts[0]

    @property
    def twos(self) -> int:
        """
        Calculate the score for the twos category

        Returns: 
            int: The sum of all dice showing 2 
        """
        return self.counts[1] * 2

    @property
    def threes(self) -> int:
        """
        Calculate the score for the threes category

        Returns: 
            int: The sum of all dice showing 3 
        """
        return self.counts[2] * 3

    @property
    def fours(self) -> int:
        """
        Calculate the score for the fours category

        Returns: 
            int: The sum of all dice showing 4 
        """
        return self.counts[3] * 4

    @property
    def fives(self) -> int:
        """
        Calculate the score for the fives category

        Returns: 
            int: The sum of all dice showing 5 
        """
        return self.counts[4] * 5

    @property
    def sixes(self) -> int:
        """
        Calculate the score for the sixes category

        Returns: 
            int: The sum of all dice showing 6 
        """
        return self.counts[5] * 6

    @property
    def three_of_a_kind(self) -> int:
        """
        Calcualte the score for the three of a kind category

        Returns:
            int: The sum of all dice if there are at least three dice showing the same number, 0 otherwise.
        """
        return sum(self.dice) if max(self.counts) >= 3 else 0

    @property
    def four_of_a_kind(self) -> int:
        """
        Calcualte the score for the four of a kind category

        Returns:
            int: The sum of all dice if there are at least four dice showing the same number, 0 otherwise.
        """
        return sum(self.dice) if max(self.counts) >= 4 else 0

    @property
    def full_house(self) -> int:
        """
        Calculate the score for the full house category

        Returns:
            int: 25 if the roll contains botha pair and three of a kind, 0 otherwise.
        """
        return 25 if 2 in self.counts and 3 in self.counts else 0

    @property
    def small_straight(self) -> int:
        """
        Calculate the score for the small straight category

        Returns: 
            int: 30 if the roll contains a sequence of four consecutive numbers, 0 otherwise. 
        """

        return 30 if any(all(i in self.dice for i in range(j, j+4)) for j in range(1, 4)) else 0

    @property
    def large_straight(self) -> int:
        """
        Calcualte the score of the large straight

        Returns:
            int: 40 if the roll contains a sequence of five consecutive numbers, 0 otherwise. 
        """
        return 40 if any(all(i in self.dice for i in range(j, j+5)) for j in range(1, 3)) else 0

    @property
    def yahtzee(self) -> int:
        """
        Calculate the score for the Yahtzee category

        Returns:
            int: 50 if all five dice show the same number, 0 otherwise. 
        """
        return 50 if 5 in self.counts else 0

    @property
    def chance(self) -> int:
        """
        Calcaute the score for the Chance category

        Returns:
            int: the sum of all dice.
        """
        return sum(self.dice)

    def score_as(self, type: Type) -> int:
        """
        Score the roll as a specific category. 

        Args: 
            type (Type): the scoring category to use.

        Returns: 
            int the score for the roll when scored as the specified category. 
        """
        return getattr(self, type.name.lower())

    @property
    def best_upper(self) -> Type:
        """
        Determine the best scoring category out of Aces, Twos, Threes, Fours, Fives, and Sixes.

        Returns:
            Type: the Type enum representing the category for this roll
        """
        upper_scores = [(Type(i), getattr(self, Type(i).name.lower()))
                        for i in range(1, 7)]
        return max(upper_scores, key=lambda x: x[1])[0]

    @property
    def best_lower(self) -> Type:
        """
        Determine the best scoring category out of three of a kind, four of a kind, full house, small straight, large straight, yahtzee, and chance

        Returns:
            Type: the Type enum representing the category for this roll

        """
        lower_types = [Type.YAHTZEE, Type.LARGE_STRAIGHT, Type.SMALL_STRAIGHT,
                       Type.FULL_HOUSE, Type.FOUR_OF_A_KIND, Type.THREE_OF_A_KIND, Type.CHANCE]
        lower_scores = [(t, getattr(self, t.name.lower()))
                        for t in lower_types]
        return max(lower_scores, key=lambda x: x[1])[0]
