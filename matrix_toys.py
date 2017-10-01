import csv

from algorithms import MatrixHighestPoints
from entities import OwnerSet

numberOfChoices = 2

print "data/hp-non-optimal.csv:"
owners = OwnerSet.importFromCsv('data/hp-non-optimal.csv')
alg = MatrixHighestPoints(owners, numberOfChoices)
config = alg.findConfiguration()
if config is not None:
    config.prettyPrint()
else:
    print "No solution found."

print "\ndata/hp-no-solution.csv:"
owners = OwnerSet.importFromCsv('data/hp-no-solution.csv')
alg = MatrixHighestPoints(owners, numberOfChoices)
config = alg.findConfiguration()
if config is not None:
    config.prettyPrint()
else:
    print "No solution found."
