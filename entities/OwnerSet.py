from Champion import Champion
from Owner import Owner

import csv

class OwnerSet:
    """Used to 1) set up the list of owners and 2) provide an array."""
    def __init__(self):
        """
        Constructor takes no parameters, sets up an owner hash table. Use a hash
        table in order to easily check for an owner's existence when reading the
        data from csv and adding champions.
        """
        self.owners_ = {}

    def __repr__(self):
        """Format used to print to the console for debugging."""
        return '{}: {}'.format(self.__class__.__name__, self.owners_)

    def getOrAddOwner(self, ownerName):
        """
        Checks if an owner exists and if not, creates one given the provided
        owner name. Returns the owner object.
        """
        if ownerName in self.owners_.keys():
            return self.owners_[ownerName]
        else:
            self.owners_[ownerName] = Owner(ownerName)
            return self.owners_[ownerName]

    def sortOwnerChampions(self):
        """Iterates over all owners and sorts their champions by PI."""
        for _, o in self.owners_.items():
            o.sortChampions()

    def getOwnerArray(self):
        """Provides the array of owners to be used by the algorithm."""
        return [o for _, o in self.owners_.items()]

    @staticmethod
    def importFromCsv(file='data/example-data.csv'):
        """
        Imports the data from CSV. The expected format of the data is:
          column 0: Champion Name
          column 1: Owner Name
          column 2: Champion PI
        """
        owners = OwnerSet()
        with open(file, 'rb') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            for row in data_reader:
                champion = Champion(row[0], int(row[2]))
                owner = owners.getOrAddOwner(row[1])
                owner.addChampion(champion)
        owners.sortOwnerChampions()
        return owners
