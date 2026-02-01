# Learning Objective: Build a Python program that generates new text
# in the style of a given training corpus using a Markov chain.
# This tutorial will teach you the fundamentals of Markov chains for text generation.

import random
from collections import defaultdict

def build_markov_chain(text: str, order: int = 2) -> dict:
    """
    Builds a Markov chain dictionary from a given text corpus.

    Args:
        text (str): The input text to train the Markov chain on.
        order (int): The "order" of the Markov chain.
                     An order of 1 means predicting the next word based on the previous one.
                     An order of 2 means predicting the next word based on the previous two words (better coherence).
                     This tutorial focuses on order 2 for better results.

    Returns:
        dict: A dictionary representing the Markov chain.
              Keys are tuples of (order) preceding words, and values are lists of possible next words.
              Example for order 2: {('the', 'quick'): ['brown', 'dog'], ('quick', 'brown'): ['fox', 'cat']}
    """
    # Initialize a defaultdict. A defaultdict is like a regular dictionary,
    # but if you try to access a key that doesn't exist, it automatically
    # creates it with a default value (in this case, an empty list).
    # This is very convenient because we don't need to check if a key exists
    # before appending a new word to its list of successors.
    markov_chain = defaultdict(list)

    # Convert the input text to lowercase to treat "The" and "the" as the same word.
    # This helps in building a more robust chain by treating word forms uniformly.
    # Then, split the text into individual words based on spaces.
    words = text.lower().split()

    # We need at least 'order + 1' words to form an initial state and a successor.
    # If the text is too short for the specified order, we cannot build a meaningful chain.
    if len(words) < order + 1:
        print("Warning: Text too short to build a Markov chain of the specified order.")
        return markov_chain

    # Iterate through the words to build the chain.
    # We stop 'order' words before the end because we need 'order' words for the key (current state)
    # and one more word for the value (the next word).
    for i in range(len(words) - order):
        # The 'state' of our Markov chain is the tuple of the 'order' preceding words.
        # For order=2, this means a tuple like (words[i], words[i+1]).
        # A tuple is used here because dictionary keys must be immutable (lists are mutable).
        current_state = tuple(words[i : i + order])

        # The 'next_word' is the word immediately following our current_state in the original text.
        next_word = words[i + order]

        # Add the 'next_word' to the list of possible continuations for the 'current_state'.
        # This builds the probabilistic transitions of our Markov chain.
        markov_chain[current_state].append(next_word)

    return markov_chain

def generate_text(markov_chain: dict, length: int = 50, order: int = 2) -> str:
    """
    Generates new text using the trained Markov chain.

    Args:
        markov_chain (dict): The Markov chain built by build_markov_chain.
        length (int): The desired number of words in the generated text.
        order (int): The order of the Markov chain (must match the order used to build the chain).

    Returns:
        str: The newly generated text.
    """
    # Ensure the chain is not empty before attempting to generate text.
    # If the chain is empty, we cannot generate any text.
    if not markov_chain:
        return "Cannot generate text: Markov chain is empty."

    # Start the text generation by picking a random initial state (a key from our chain).
    # We convert markov_chain.keys() to a list to allow random.choice to pick an element.
    current_state = random.choice(list(markov_chain.keys()))

    # Initialize our generated text with the words from our starting state.
    # The '*' unpacks the tuple `current_state` into individual arguments for `list()`'s constructor,
    # effectively creating a list of the words from the starting state.
    generated_words = list(current_state)

    # Loop to generate the rest of the words until we reach the desired length.
    while len(generated_words) < length:
        # Check if our current_state exists as a key in the Markov chain.
        # It might not exist if we've reached an 'end' of a sequence
        # that doesn't have a defined successor in the training corpus.
        if current_state in markov_chain:
            # Randomly choose the next word from the list of possibilities
            # associated with the current state. This is the core of the generation process.
            next_word = random.choice(markov_chain[current_state])
            generated_words.append(next_word)

            # Update the current state for the next iteration.
            # We shift the window one word forward: the new state consists of the last 'order' words.
            # For order=2, if current_state was (word1, word2) and next_word is word3,
            # the new state becomes (word2, word3).
            current_state = tuple(generated_words[-order:])
        else:
            # If the current state has no known successor, we've hit a dead end.
            # This means the training corpus didn't contain any word following this specific sequence.
            # For simplicity, we stop generating text here. In more advanced scenarios,
            # you might restart with a new random state or try backtracking.
            print(f"Reached a dead end with state {current_state}. Stopping text generation.")
            break

    # Join the list of generated words back into a single string, separated by spaces.
    return " ".join(generated_words)

# --- Example Usage ---

if __name__ == "__main__":
    # Define a sample text corpus. The quality and style of the generated text
    # are highly dependent on the training corpus.
    # A larger and more diverse corpus will generally lead to more varied and coherent output.
    # Punctuation is kept for simplicity, but in a real-world application,
    # you might preprocess it (e.g., remove, replace with special tokens, or treat as words).
    corpus_text = (
        "The quick brown fox jumps over the lazy dog. The dog barks loudly. "
        "The quick fox is very fast. Brown dogs are often lazy. "
        "A quick brown fox can outsmart a lazy dog. The dog and the fox are friends. "
        "This is a simple example to demonstrate the markov chain principle."
        "A truly quick brown fox will always outsmart a truly lazy dog. "
        "The fox saw the dog, and the dog saw the fox. They were both quick."
    )

    print("--- Building Markov Chain ---")
    # Build the Markov chain model from our corpus.
    # We use 'order=2', meaning the model considers the two preceding words
    # when determining the next word, which typically produces more coherent sentences
    # than an order 1 chain (which only looks at the immediately preceding word).
    markov_chain_model = build_markov_chain(corpus_text, order=2)

    # Optional: You can uncomment the lines below to inspect a small part of the
    # generated Markov chain to understand its structure.
    # print("\nSample of Markov Chain (first 5 entries):")
    # for i, (state, successors) in enumerate(markov_chain_model.items()):
    #     if i >= 5:
    #         break
    #     print(f"  {state} -> {successors}")

    print("\n--- Generating Text ---")
    # Generate text of a specified length (e.g., 30 words) using our trained model.
    # Experiment with different lengths to see how the generated text changes.
    generated_text = generate_text(markov_chain_model, length=30, order=2)

    print("\nGenerated Text:")
    print(generated_text)
    print("\n--- End of Tutorial ---")

    # You can try generating text again with a different length or even a different order
    # (remember to rebuild the chain if changing the order).
    # generated_text_longer = generate_text(markov_chain_model, length=60, order=2)
    # print("\nGenerated Text (longer):")
    # print(generated_text_longer)