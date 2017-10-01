class CombinationIterator:
    """
    Class used to iterate through all possible k-combinations of n elements of
    an array.
    """
    def __init__(self, inputArray, numberOfChoices):
        """
        Constructor takes an input array (with n elements) and a number of
        possible choices (k).
        """
        self.rawArray_ = inputArray
        self.setNumberOfChoices(numberOfChoices)
        self.resetIteration()

    def setNumberOfChoices(self, numberOfChoices):
        """Sets the number of choices parameter (k)."""
        self.numberOfChoices_ = numberOfChoices
        if (self.numberOfChoices_ > len(self.rawArray_)):
            raise Exception(
                'Cannot choose ' + self.numberOfChoices_ + ' elements from a ' +
                len(self.rawArray_) + ' element array.')

    def getNumberOfChoices(self):
        """Returns the number of choices parameter (k)."""
        return self.numberOfChoices_

    def resetIteration(self):
        """Resets the iteration."""
        self.indexes_ = range(0, self.numberOfChoices_)

    def addElement(self, element):
        """Adds an element to the raw array for iteration."""
        self.rawArray_.append(element)

    def getCurrentCombination(self):
        """
        Get the current combination. If indexes_ is None, return None since this
        means we've iterated through all possible combinations.
        """
        if self.indexes_ is None: return None
        return [self.rawArray_[index] for index in self.indexes_]

    def next(self):
        """Provides the next possible combination in the iteration."""
        self.updateIndexes_()
        return self.getCurrentCombination()

    def updateIndexes_(self):
        # Update the array of indexes.
        maxPossible = len(self.rawArray_) - 1
        metaIndex = self.numberOfChoices_ - 1
        self.updateIndex_(metaIndex, maxPossible)        

    def updateIndex_(self, metaIndex, maxPossible):
        # Base case. If we ever get to a negative meta index, stop recursion.
        if metaIndex < 0:
            self.indexes_ = None
            return -1

        # Try to increment the current index. If we get past the maximum
        # possible index, recurse on a lower meta index.
        index = self.indexes_[metaIndex] + 1
        if index > maxPossible:
            # The recursive function call will return the the value of the
            # lower meta index. This one must be one more than that.
            index = self.updateIndex_(metaIndex - 1, maxPossible - 1) + 1
            # If the lower meta index returned -1, don't try to update indexes
            # since the indexes_ array is None.
            if index < 0: return -1

        # Update the index and return it's value for the next level in the
        # recursion stack.
        self.indexes_[metaIndex] = index
        return index

