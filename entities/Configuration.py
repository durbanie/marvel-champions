class Configuration:
    """Holds a configuration of owners and the champions they have chosen."""

    def __init__(self):
        """Constructor takes no parameters. Sets up the configuration hash."""
        self.config_ = {}
        self.used_ = set([])
        self.powerIndex_ = 0

    def __repr__(self):
        """Format used to print to the console for debugging."""
        return 'PI: {}, Configuration: {}'.format(
            self.powerIndex_, self.config_)

    def setOwnerConfig(self, ownerName, champions, powerIndex):
        """Adds the owner-config to the global configuration."""
        self.config_[ownerName] = champions
        for c in champions:
            self.used_.add(c.getType())
        self.powerIndex_ += powerIndex

    def updateOwnerConfig(self, ownerName, champion):
        """Updates the owner configuration with a single champion."""
        if self.haveOwner(ownerName):
            self.config_[ownerName].append(champion)
        else:
            self.config_[ownerName] = [champion]
        self.used_.add(champion.getType())
        self.powerIndex_ += champion.getPowerIndex()

    def haveOwner(self, ownerName):
        """
        Checks if the configuration already contains a particular ownerName.
        """
        return ownerName in self.config_;

    def getUsed(self):
        """Returns the set of types currently used by this configuration."""
        return self.used_

    def getPowerIndex(self):
        """Returns the total power index for this configuration."""
        return self.powerIndex_

    def getOwnerNumChampions(self, ownerName):
        """Returns the number of choices the ownerName has already made."""
        if self.haveOwner(ownerName):
            return len(self.config_[ownerName])
        return 0

    def prettyPrint(self):
        """Prints the configuration in a nicer format."""
        for o in self.config_.keys():
            print o
            champs = self.config_[o]
            for c in champs:
                print '\t{}'.format(c)
        print 'Total PI: {}'.format(self.powerIndex_)
        print 'Champs Used: {}'.format(len(self.used_))
