# Day 24

Our assumption is that when we have a partially correct solution,
then a part of the output bits will also be correct. This implies
we can converge towards a correct solution by reusing parts of the
partial solution.

We tried two methods: a Genetic Algorithm and an exhaustive search
to cumulatively add more pairs.

## Genetic Algorithm

First we create a list of randomly generated swap patterns. This is
our first "generation".

Next we grow a new generation using these operations (retrying each
 time we get a duplicate that is already in the generation):

- in 60% of the cases we randomly select two swap patterns and create
  a new swap pattern by randomy using pieces either two.

- in 30% of the cases we randomly select a swap pattern and replace
  one of the swap by a new random swap.
  
- in 10% of the cases we generate a completely new random swap pattern.

The new generation is much larger that the old generation. For each
swap pattern we calculate the number of invalid output bits. We select
the best swap patterns from the new generation and start the next 
iteration.

This algorithm does converge very slowly and might not ever find the
solution. When we noticed this, we started coding the exhaustive search
method below.

## Exhaustive search for pairs

We exhaustively search all combinations of two gates to swap and 
measure which pair gives the lowest number of invalid output bits.
We keep the best pair, and start searching for the second pair by 
again measuring the number of invalid output bits. 

We keep adding pairs until we have the right amount of pairs. If
that was not yet the solution, we remove the oldest pair and try
to add a new pair.
