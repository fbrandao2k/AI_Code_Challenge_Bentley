Part 1: Text Generation - Markov Chain Problem
Introduction
Most text generation AI models, including LLMs such as GPT-4, produce text by sampling from a probability distribution over the next words to continue a sentence. A simple example is a Markov Chain, represented by a weighted graph where nodes are words and edges lead to next words with probability equal to the edge weight. 
Problem Statement
Given a Markov Chain as a weighted directed acyclic graph, what is the longest sequence (sentence) through the Markov Chain possible? 

The Markov Chain is given as a JSON file: https://tinyurl.com/vvndt88h
The JSON file represents the Markov Chain in adjacency list format. Each of the top-level keys represent nodes/words and map to another object/dict whose keys are all the possible words that could come next, and whose values are the edge weights.
A sequence/sentence starts with the node "START" and ends once the "END" node is reached.
Length of a sequence/sentence is measured in the number of words (excluding "START" and "END").

Example
The following example JSON file, https://tinyurl.com/5k52fpxk,  represents the following possible sentences:
Hooray for AI and ML. (probability 30%)
Hooray for holidays. (probability 30%)
Yay for AI and ML. (probability 20%)
Yay for puzzles. (probability 20%)
The longest sentence is "Yay for AI and ML", with 5 words.

Part 2: Average Sentence Length -> Monte Carlo Simulation Problem
Introduction
Let's try something a step up in difficulty. Let's actually work with the probability distribution of our Markov Chain.

Problem Statement
Given a Markov Chain as a weighted directed (not necessarily acyclic) graph, what is the average sentence length? As in Part 1, length is measured in number of words (excluding "START" and "END").

The Markov Chain (which was generated from Bentley's press releases!) is given as an adjacency list JSON file: https://tinyurl.com/43pu74r5 
Round your answer to 2 decimal places.

Example

The following example JSON file, https://tinyurl.com/mu5efpvz,  represents the following possible sentences:
Hooray for AI and ML. (probability 30%)
Hooray for puzzles. (probability 30%)
Yay for AI and ML. (probability 20%)
Yay for puzzles. (probability 20%)
The average sentence length is 5 * 0.3 + 3 * 0.3 + 5 * 0.2 + 3 * 0.2 = 4.00 words.

