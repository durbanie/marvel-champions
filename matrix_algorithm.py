import csv

from algorithms import MatrixHighestPoints
from algorithms import MatrixHighestPointsLowestPlayers
from entities import OwnerSet

numberOfChoices = 5
owners = OwnerSet.importFromCsv('data/example-data.csv')
alg = MatrixHighestPointsLowestPlayers(owners, numberOfChoices)
config = alg.findConfiguration()
if config is not None:
    config.prettyPrint()
else:
    print "No solution found."
