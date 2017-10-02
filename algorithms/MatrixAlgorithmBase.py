import abc
from entities import Configuration

class MatrixAlgorithmBase:
    """
    Base class for a matrix style algorithm. This class chooses a configuration
    as follows:
      1) For M owners each with a pool of N champions, create an MxN matrix.
      2) Iterate through each element (champion) in the matrix and score each
         champion according to some heuristic (e.g. negative of the maximum
         number of points). The score should be interpreted as a "cost" of
         choosing a particular champion for a particular owner.
      3) Choose the champion with the minimum cost (e.g. for the example
         heuristic above, it would be the champion with the maximum number of
         points of all elements in the MxN matrix).
      4) Once a choice is made, remove all other champions of the same type that
         are left in the matrix so that we never choose the same champion twice.
      5) Repeat steps 2-4 until either a) we arrive at a solution (the solution
         is "complete") or b) we arrive at a case where no solution is possible
         because a given owner doesn't have enough remaining champions.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, ownerSet, numberOfChoices):
        """
        The algorithm solves a problem defined by:
          1) The set of owners (ownerSet) along with their array of champions.
          2) The number of choices (numberOfChoices) each owner must make to
             complete the configuration.
        """
        self.owners_ = ownerSet.getOwnerArray()
        self.config_ = Configuration()
        self.numberOfChoices_ = numberOfChoices

    @abc.abstractmethod
    def cost(self, owner, champion):
        """
        The cost function to be implemented in sub-classes which drives the
        choice of champion from the matrix.
        """
        pass

    def findConfiguration(self):
        """
        This is the only external call a consumer should make after creating
        the object. This will continue choosing the next champion until either
        the solution is complete.
        """
        while self.isSolutionPossible() and not self.isSolutionComplete():
            self.chooseNext_()
        if self.isSolutionComplete():
            return self.config_
        return None

    def chooseNext_(self):
        """
        Chooses the next champion by iterating through all remaining champions,
        scoring each according to the heuristic, and adding the owner/champion
        pair with the minimum score.
        """
        used = self.config_.getUsed()
        minScore, minOwner, minChampion = None, None, None
        for o in self.owners_:
            for c in o.getAvailableChampions(used):
                score = self.cost(o, c)
                if minScore is None or score < minScore:
                    minScore, minOwner, minChampion = score, o, c
        self.config_.updateOwnerConfig(minOwner.getName(), minChampion)

    def isSolutionComplete(self):
        """
        Checks if we've finished making the necessary number of choices for each
        owner.
        """
        for o in self.owners_:
            remaining = self.remainingNumberOfChoices(o)
            if remaining > 0:
                return False
        return True

    def isSolutionPossible(self):
        """
        Checks if it is still possible to make necessary number of choices.
        """
        used = self.config_.getUsed()
        for o in self.owners_:
            remaining = self.remainingNumberOfChoices(o)
            if remaining > len(o.getAvailableChampions(used)):
                return False
        return True

    def remainingNumberOfChoices(self, owner):
        return (self.numberOfChoices_ - 
                self.config_.getOwnerNumChampions(owner.getName()))

    def getRemainingChampions(self, owner):
        used = self.config_.getUsed()
        return owner.getAvailableChampions(used)
