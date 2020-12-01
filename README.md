# Advent of Code 2020
Solving puzzles of AoC20, probably all with Python. 

Fourth year I'm joining this cool challenge. Goal is just to solve 
every puzzle within the day. Last year I focused on the use of Python and writing 
Pythonic code (check my other repos). 

This year I just solve the problems. Hopefully I can find the time
to complete it.

In this readme, just some notes about the puzzles, my code and other 
solutions I have seen. All solution can be found in this repository.

## [--- Day 1: Report Repair ---](https://adventofcode.com/2020/day/1)
Not much to see here.. really easy first puzzle today. The biggest 
challenge today was getting my wifi working. Unfortunately we got an
electrical issue by a short circuit somehwere in the house. Haven't 
figured it out. But managed to get on the internet for a couple of
minutes, which was enough to solve this one!

P1: out of a list of numbers, find the two numbers that sum to 2020.
P2: out of a list of numbers, find the three elements that sum to 2020.

Just created a list of possible combinations and checked them. The 
result came in directly. Easy..

But the guys from our AoC-slack-group came up with creative and optimal
solutions for part 1.

One was based on first sorting the list and using two counters (one
at the beginning of the list and one at the end). If the sum is bigger
than 2020, move the endcounter one to the left, if the sum is smaller
than 2020, move the begincounter one to the right (O(n\*log(n)). Credits
to Mario.

The other solution was to create a set of the numbers. Then iterate 
through the numbers and check if "2020-number" is in the set. Using a
set makes it cheap to get the element, which results in O(n) as time
complexity for part 1. Credits to [Chris][https://github.com/Chriskamphuis/aoc2020].
