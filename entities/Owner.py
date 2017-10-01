from Champion import Champion
from CombinationIterator import CombinationIterator

class Owner:
    """Class used to represent an owner."""

    def __init__(self, name):
        """
        Constructor requires a string name and initializes the owner's list of
        champions to an empty array.
        """
        self.name_ = name
        self.champions_ = []

    def __repr__(self):
        """Format used to print to the console for debugging."""
        return '{}: {} - {}'.format(
            self.__class__.__name__, self.name_, self.champions_)

    def getName(self):
        """Returns the name of the owner."""
        return self.name_

    def addChampion(self, champion):
        """Adds a champion to this owner."""
        self.champions_.append(champion)

    def sortChampions(self):
        """Sorts the owner's champions in descending order by PI."""
        self.champions_ = sorted(
            self.champions_, key=lambda c: c.getPowerIndex(), reverse=True)

    def getAvailableChampions(self, used=set([])):
        """
        Provides an array of this owner's available champions that are NOT in
        the "used" set. "used" is a hash set so that checking for inclusion in
        the set should be efficient.
        """
        # Since the self.champions_ array is already sorted, iterate through the
        # array and check if the type is already in used. If not, include in the
        # array to return.
        return [c for c in self.champions_ if c.getType() not in used]

    def getAvailableChampionsIterator(self, numberOfChoices, used=set([])):
        """
        Provides an iterator of this owner's available champions. The
        iterator will transparently allow iteration through all possible
        k-combinations of the available champions array (without the need for
        nested for loops), where "k" = numberOfChoices.
        """
        return CombinationIterator(
            self.getAvailableChampions(used), numberOfChoices)
