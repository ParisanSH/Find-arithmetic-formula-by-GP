# Find-arithmetic-formula-by-GP
Genetic Programming has been used in a variety of fields to solve difficult problems and produce human competitive results. In the field of mathematics, it has been used to solve problems such as symbolic regression, the discovery of trigonometry identities, and sequence induction, just to name a few (Koza 1992).

In this mini project, been written a program that can get any formulas using GP. For example, you have to create the following statement: 

X^2 +2X + 1

This equation can be represented by the following three:
For simplicity, assume that in each formula only the symbol X is available and we're allowed to build a formula using four operators (+ - * /).

![image](https://user-images.githubusercontent.com/14861041/210171897-001e621b-b71f-430d-8462-82f356e3995f.png)

# Consideration:
1. A population of programs expressed is maintained (e.g, strings of arithmetic expressions in the above case).

2. At least one search operator is used in order to produce new candidate programs, e.g.

    - a mutation operator that replaces a randomly selected instruction in a program with another random instruction,
    - a mutation operator that appends a randomly selected instruction to
    - a program,
    - a crossover operator that slices two parent programs at two random locations and swaps the ‘tails’,
3. The search is driven by using a straightforward fitness function, like the number of examples/tests on which the program behaves correctly.
