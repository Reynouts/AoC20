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
complexity for part 1. Credits to [Chris](https://github.com/Chriskamphuis/aoc2020).

## [--- Day 2: Password Philosophy ---](https://adventofcode.com/2020/day/2)
Easy puzzle today again. I guess even less discussion about complexity
than day 1. Input are a list of password, including a two numbers and a letter.

P1: count frequency of a given letter in password and see if it falls within
a given range (the two numbers)
P2: Use the two numbers as indexes and check if exactly one of those places
contain the given letter.

I do both parts in one go. In a line by line loop I first parse the input 
(I just used split() and map)) then check the frequency of the given letter
in the password and if it is in the given range. Next I do the XOR (in Python
you can use `^` or `!=`) check for the positions. 

You could add try/catch stuff for the indexing of the passwords to be failsafe
and you could bail out early when the frequency is hihger than the high limit
of the range for some optimization, but that's about it I guess!

## [--- Day 3: Toboggan Trajectory ---](https://adventofcode.com/2020/day/3)
A typical AoC puzzle, which I really like. You get a sort of topdown map as
input and need to map out a trajectory and see what is in the way of the
trajectory. This time there are trees on a slope and you want to select the
best route with your toboggan, based on the trees you can avoid on the slope.

The map repeats itself in horizontal direction. You only have to store the
object locations which you can hit or need to count (in this specific case,
only the trees) and the toboggan just moves linear according to some given
slope. This makes it easy to check which trees the toboggan hits in its 
trajectory on the slope.

No problems solving this one, but I liked it. And every year I try to make
some fun visualisations in the basic commandprompt/terminal. So this was a
nice opportunity to create one!

![giffie](day3_up.gif)

## [--- Day 4: Passport Processing ---](https://adventofcode.com/2020/day/4)
Today a bit more elbow grease: validation of passport fields. This could for
a part done with regexes, but I could not manage to put it all in a regex.
I used a dictionary with the passport fields as keys and as values function
pointers or lambda functions if they were short.

I did found out that python dictionaries are ordered since python 3.7 and 
that I found the wallrus operator useful (but it's only from 3.8!).

In the meantime I check out some old 2015/2016 puzzles. I participated and
completed 2017/2018/2019, so I want to have those stars ;)

Let's head into the weekend!