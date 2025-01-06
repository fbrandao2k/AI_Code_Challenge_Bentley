Part 1: Connected Cities
Introduction
At Bentley we connect teams with software for infrastructure. Can AI help us design and optimize these solutions?

Problem Statement
Given a distance matrix representing distances between all pairs of cities, what is the minimum total distance of a network connecting all of them? 
An edge in your network must be between 2 cities, and a pair of cities is considered connected if there is a connected path through your network between them.

The distance matrix is given as a csv file: https://tinyurl.com/4znspvnn

Example
Let's take a look at how we would connect the following cities:
Exton, Pennsylvania
Montreal, Quebec
Quebec City, Quebec
Toronto, Ontario
New York City, New York
San Francisco, California
The distances between them are given in the following csv file: https://tinyurl.com/s798umjf
The minimum sized network connecting all of these cities would be Exton-Toronto (509795m), Exton-New York City (157066m) Montreal-Quebec City (233039m) Montreal-Toronto (504182m) Toronto-San Francisco (3643511m), for a total of distance of 5047593m.


Part 2: Traffic
Introduction
Let's try something a step up in difficulty. Instead of connecting cities with a minimal network, let's look at the maximum traffic flow between cities, a problem very relevant to many Bentley teams.

Problem Statement
Given a weighted directed       graph representing a road network with road capacities, what is the       maximum traffic flow between city 'A' and the city 'Z'?

The graph is given as an adjacency list JSON file: https://tinyurl.com/mpax5zjb
Round your answer to 2 decimal places.

Example
The following example JSON, https://tinyurl.com/2sax8u8f, represents the following cities:
City A has a road leading to city B, with a capacity of 10
City A has a road leading to city C, with a capacity of 10
City B has a road leading to city D, with a capacity of 3
City C has a road leading to city D, with a capacity of 2
City D has a road leading to city Z, with a capacity of 6
The traffic flow is limited by the roads between B and D, and C and D, which gives a maximum traffic flow of 5.00.
