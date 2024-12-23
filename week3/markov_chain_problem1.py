import json

def load_markov_chain(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_phrases(chain, current_word='START', current_phrase=[], current_prob=1.0):
    if current_word == 'END':
        phrase = ' '.join(current_phrase[:-1])  # Exclude 'END' from the phrase
        yield (phrase, len(current_phrase) - 1, current_prob)  # Exclude 'END' from the word count
    else:
        for next_word, prob in chain.get(current_word, {}).items():
            yield from generate_phrases(chain, next_word, current_phrase + [next_word], current_prob * prob)

def main(file_path):
    chain = load_markov_chain(file_path)
    phrases = list(generate_phrases(chain))
    for phrase, word_count, prob in phrases:
        print(f"Phrase: '{phrase}', Words: {word_count}, Probability: {prob:.4f}")
    
    # Find the phrase with the largest number of words
    longest_phrase = max(phrases, key=lambda x: x[1])
    print(f"\nLongest Phrase: '{longest_phrase[0]}', Words: {longest_phrase[1]}, Probability: {longest_phrase[2]:.6f}")

if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with your file path
    main(file_path)