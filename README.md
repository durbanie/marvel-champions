# Marvel Contest of Champions - Uniqueness Problem

## Prerequisites

This code requires python 2.7: https://www.python.org/downloads/

To run, enter the following at the command line:

%> python matrix_algorithm.py

## Overview

### The Problem

The problem this code tries to solve is this:

Given *M* players (or owners) in an alliance, each with *N* champions (e.g. Thor, Venom, Captain America, etc.) with various "Power Index" or "PI" ratings, can you assign *k* champions per owner such that each assigned champion is unique (i.e. no two owners are assigned the same champion)?

Assuming a solution exists, ideally we want to find the solution that maximizes the total power index (i.e. the "optimal solution").

### Battlegroup Variation

I'm now told that the uniqueness doesn't need to be across the entire alliance, rather within individual "battle groups". This actually makes finding the "optimal" solution much more difficult as it adds additional combinatorics (see the Brute Force section below).

## Strategies

### Brute Force

The naive brute force solution (iterating through all possible combinations and checking that the solution is valid and produces the maximum) for this problem is impractical. Each player needs to select *k* champions from *N* possible elements, without repetition and the order of selection does not matter. Mathematically, this is a combination and it's value is given by the binomial coefficient, or "N-choose-k" (*NCk*):

*NCk = N! / (k! x (N - k)!)*

Since we have *NCk* combinations for each of *M* owners, there are a total of *NCk^M* combinations to iterate through for the naive solution. 

Now, let's look at practical values for *M*, *N*, and *k*. My Dad's alliance has *M*=30 players, each of which have roughly *N*=30 high PI champions. For an alliance war, each player would send *k*=5. Therefore:

* Each owner has 30-choose-5 = 142,506 possible combinations.
* The entire alliance (therefore) has 142,506^30 = 4x10^154 possible combinations.

Assuming (for the sake of the argument) that a typical computer operating at ~10 GHz evaluates one combination every cycle, it would take ~10^144 seconds to evaluate all possible combinations, which is ~10^137 years (hundreds of orders of magnitude longer than the estimated age of the universe, which is only a mere 1.4x10^10 years old).

#### Brute Force for the Battlegroup Variation

In this case, we divide the alliance into 3 equal battlegroups of 10 owners. For the first battlegroup, we have 30 possible owners, so we have 30-choose-10 = ~30 million combinations. For the second battle group, we need to choose 10 players from the remaining 20, so there are 20-choose-10 = 185 thousand combinations. The remaining 10 would be assigned to the last battlegroup. 

So we have 30 million times 185 thousand, which is about 5.5 trillion possible battlegroup combinations. This actually double counts many configurations (e.g. this counts a particular configuration in battlegroup 1 and another in battlegroup 2 as a separate instance from one where the two identical configurations switch battlegroups). To be precise, this overcounts by a factor 3!=6, so there is actually about 925 billion battlegroup combinations.

We need to multiply that by the 4x10^154 possible combinations from the original problem, giving us a grand total of 3.8x10^166 possible combinations for the variation!

### Matrix Strategy

The matrix strategy chooses a configuration as follows:

1) For *M* owners each with a pool of *N* champions, create an *MxN* matrix.
2) Iterate through each element (champion) in the matrix and score each champion according to some heuristic (e.g. negative of the maximum number of points). The score should be interpreted as a "cost" of choosing a particular champion for a particular owner.
3) Choose the champion with the minimum cost (e.g. for the example heuristic above, it would be the champion with the maximum number of points of all elements in the MxN matrix).
4) Once a choice is made, remove all other champions of the same type that are left in the matrix so that we never choose the same champion twice.
5) Repeat steps 2-4 until either a) we arrive at a solution (the solution is "complete") or b) we arrive at a case where no solution is possible because a given owner doesn't have enough remaining champions in their pool.

#### Implementation

A MatrixAlgorithmBase class implements much of the details of this algorithm, except for the cost function. This (abstract) method should be implemented in sub-classes, an example of which is MatrixHighestPoints, which defines the cost as the negative of the PI of each remaining champion for each owner that still needs to make the requisite choices. If an owner has already made all *k* choices, define the cost as 0 for each of their champions, which will always be greater than the cost of other eligible owner's champions and so will never be chosen.

The algorithm does find a solution for the example data set for *k*=5.

#### Optimal Solution Correctness

Whether or not the solution is optimal depends on the cost function. For the simple "highest points" implementation, the algorithm is neither guaranteed to find the optimal solution, nor a solution at all, even if one exists. See the two toy examples in the "data" directory. In each case, there are 2 owners with 3 or 4 champions, and we impose that each owner must select 2 champions.

hp-non-optimal.csv: The optimal solution, by inspection, is for Owner1 to choose champ3 & champ4 and Owner2 to choose champ1 & champ2, for a total of 350 PI. However, the algorithm reverses these for a total of 310 PI.

hp-no-solution.csv: In this case, a solution actually exists: Owner1 chooses champ1 and champ3 and Owner2 chooses champ2 and champ4. However the algorithm greedily chooses champ1 and champ2 for Owner1, leaving only champ4 for Owner2 which leaves no solution.

On the test data (data/example-data.csv), the highest points matrix algorithm yields a solution with a total PI of 246,504. Note that if we were to choose the top 5 champions from each owner (regardless of uniqueness), the total PI would be 263,811, only ~17,000 points higher. The optimal solution on this particular dataset must be less than this, so our matrix algorithm is likely fairly close to optimal.

#### Efficiency

The efficiency of this strategy depends on the implementation details of the cost function. The cost function will be called for each element in the matrix, for each choice. There are *Mk* choices and the matrix has at most *MN* elements. Therefore the algorithm runs as *O(M^2 N k)xO(c)*, where *O(c)* is the asymptotic runtime of the cost function.

For the highest points implementation, the cost function has constant runtime, so the algorithm runs as *O(M^2 N k)*.
