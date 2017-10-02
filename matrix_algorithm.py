import csv

from algorithms import MatrixHighestPoints
from algorithms import MatrixHighestPointsLowestPlayers
from entities import OwnerSet

numberOfChoices = 5
file='data/example-data.csv'

def run(alg):
    config = alg.findConfiguration()
    if config is not None:
        config.prettyPrint()
    else:
        print "No solution found."

owners = OwnerSet.importFromCsv(file)

print "--------------------------------------------------"
print "Matrix (highest points):"
run(MatrixHighestPoints(owners, numberOfChoices))

print ""
print "--------------------------------------------------"
print "Matrix (highest points/worst player):"
run(MatrixHighestPointsLowestPlayers(owners, numberOfChoices))
