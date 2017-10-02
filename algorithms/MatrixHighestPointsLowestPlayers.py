from MatrixAlgorithmBase import MatrixAlgorithmBase

class MatrixHighestPointsLowestPlayers(MatrixAlgorithmBase):
    """
    Implementation of MatrixAlgorithmBase that selects the champion with the
    highest points from the player with the lowest valued champion.
    """

    def cost(self, owner, champion):
        """
        In order to select the champion with the highest PI from the owner with
        the lowest-valued champion, define the cost as:
          1) If this champion is this owner's highest valued remaining champion,
             define it's cost as the positive value of the champion's PI.
          2) If this is not this owner's highest valued champion, define it's
             cost as 0.
          3) If the owner has already chosen the requisite number of choices,
             define it's cost as 0.
        """
        remaining = self.remainingNumberOfChoices(owner)
        if remaining <= 0: return 99999999
        remainingChampions = self.getRemainingChampions(owner)
        if champion == remainingChampions[0]:
            return champion.getPowerIndex() / remaining
        return 0
