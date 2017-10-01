class Champion:
    """Class used to represent a champion"""

    def __init__(self, type, powerIndex):
        """Constructor requires a string type and integer power index (PI)."""
        self.type_ = type
        self.powerIndex_ = powerIndex

    def __repr__(self):
        """Format used to print to the console for debugging."""
        return '{}: {} ({})'.format(
            self.__class__.__name__, self.type_, self.powerIndex_)

    def getType(self):
        """Returns the type or name of the champion."""
        return self.type_

    def getPowerIndex(self):
        """Returns the PI of the champion."""
        return self.powerIndex_
