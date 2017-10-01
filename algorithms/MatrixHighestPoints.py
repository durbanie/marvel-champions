from MatrixAlgorithmBase import MatrixAlgorithmBase

class MatrixHighestPoints(MatrixAlgorithmBase):
    """
    Implementation of MatrixAlgorithmBase that simply selects the champion with
    the highest PI, provided the owner of the champion still has less than the
    requisite number of selected champions.
    """

    def cost(self, owner, champion):
        """
        In order to select the champion with the highest PI, define the cost as:
          1) If the owner still hasn't selected all of their champions, return
             the negative of the champion's power index.
          2) If the owner has already selected all of their champions, return 0.
        """
        remaining = self.remainingNumberOfChoices(owner)
        return 0 if remaining <= 0 else -champion.getPowerIndex()
