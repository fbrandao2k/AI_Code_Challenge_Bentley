import json
import random

def load_markov_chain(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def simulate_markov_chain(chain, iterations=1000000):
    total_length = 0

    for _ in range(iterations):
        current_state = "START"
        length = 0

        while current_state != "END":
            next_states = chain.get(current_state, {})
            if not next_states:
                break

            # Choose the next state based on probabilities
            next_state = random.choices(
                population=list(next_states.keys()),
                weights=list(next_states.values()),
                k=1
            )[0]

            if next_state != "END":
                length += 1

            current_state = next_state

        total_length += length

    # Calculate the average length
    average_length = total_length / iterations
    return average_length

if __name__ == "__main__":
    # Replace 'input.txt' with the path to your JSON file
    markov_chain = load_markov_chain("input3.txt")

    # Number of iterations for Monte Carlo simulation
    iterations = 10000000

    average_length = simulate_markov_chain(markov_chain, iterations)
    print(f"Estimated Average Length: {average_length:.2f}")