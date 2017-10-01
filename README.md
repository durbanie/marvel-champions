# Marvel Contest of Champions - Uniqueness Problem

## Overview of the Game

## The Problem

The problem this code tries to solve is this:

Given *M* players (or owners) in an alliance, each with *N* champions (e.g. Thor, Venom, Captain America, etc.) with various "Power Index" or "PI" ratings, can you assign *k* champions per owner such that each assigned champion is unique (i.e. no two owners are assigned the same champion)?

Assuming a solution exists, ideally we want to find the solution that maximizes the total power index (i.e. the "optimal solution").

### Variation

I'm now told that the uniqueness doesn't need to be across the entire alliance, rather within individual "battle groups". This actually makes finding the "optimal" solution much more difficult as it adds additional combinatorics (see the Brute Force section below).

## Strategies

### Brute Force

The naive brute force solution (iterating through all possible combinations and checking that the solution is valid and produces the maximum) for this problem is impractical. Each player needs to select *k* champions from *N* possible elements, without repetition and the order of selection does not matter. Mathematically, this is a combination and it's value is given by the binomial coefficient, or "N-choose-k" (nCk):

*NCk = N! / (k! \. (N - k)!)*

Since we have *NCk* combinations for each of *M* owners, there are a total of *NCk^M* combinations to iterate through for the naive solution. 

Now, let's look at practical values for *M*, *N*, and *k*. My Dad's alliance has *M*=30 players, each of which have roughly *N*=30 high PI champions. For an alliance war, each player would send *k*=5. Therefore:

* Each owner has 30-choose-5 = 142,506 possible combinations.
* The entire alliance (therefore) has 142,506^30 = 4x10^154 possible combinations.

Assuming (for the sake of the argument) that a typical computer operating at 10 GHz evaluates one combination every cycle, it would take ~10^144 seconds to evaluate all possible combinations, which is ~10^137 years (hundreds of orders of magnitude longer than the estimated age of the universe, which is only a mere 1.4x10^10 years old).

### Brute Force for Variation

In this case, we divide the alliance into 3 equal battlegroups of 10 owners. For the first battlegroup, we have 30 possible owners, so we have 30-choose-10 = ~30 million combinations. For the second battle group, we need to choose 10 players from the remaining 20, so there are 20-choose-10 = 185 thousand combinations. The remaining 10 would be assigned to the last battlegroup. 

So we have 30 million times 185 thousand, which is about 5.5 trillion possible battlegroup combinations. We need to multiply that by the 4x10^154 possible combinations from the original problem, giving us a grand total of 2x10^167 possible combinations for the variation!

## Matrix Strategy
