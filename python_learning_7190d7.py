# AI Story Generator Tutorial

# Learning Objective:
# This tutorial will guide you through building a simple AI story generator in Python.
# We will focus on the core concept of using a pre-trained language model
# to generate text based on a user's initial prompt. This introduces the
# fundamental idea of prompt engineering and text generation with AI.

# --- Part 1: Setup and Importing Libraries ---

# We need a powerful library to interact with pre-trained language models.
# The 'transformers' library from Hugging Face is excellent for this.
# If you don't have it installed, run: pip install transformers
from transformers import pipeline

# --- Part 2: Loading a Pre-trained Language Model ---

# The 'pipeline' function is a high-level abstraction that makes it easy
# to use pre-trained models for various tasks.
# We're choosing the 'text-generation' task.
# 'gpt2' is a widely used and capable, but relatively small, language model
# that's great for learning and experimentation.
# The model will be downloaded the first time you run this.
print("Loading AI model... This may take a moment on the first run.")
story_generator = pipeline("text-generation", model="gpt2")
print("Model loaded successfully!")

# --- Part 3: Getting User Input (The Prompt) ---

# The "prompt" is the starting point for our AI story.
# The better the prompt, the more relevant and interesting the generated story will be.
def get_user_prompt():
    """
    Asks the user for a story idea or starting sentence.
    """
    print("\n--- Let's start your story! ---")
    prompt_text = input("Enter a sentence or a few words to start your story: ")
    return prompt_text

# --- Part 4: Generating the Story ---

# This is where the magic happens! The AI model takes our prompt and
# predicts the most likely sequence of words to follow.
def generate_story(prompt, max_length=150, num_return_sequences=1):
    """
    Generates a story using the AI model based on the provided prompt.

    Args:
        prompt (str): The starting text for the story.
        max_length (int): The maximum number of tokens (words/pieces of words)
                          the generated text can have.
        num_return_sequences (int): The number of different story variations to generate.
                                    For simplicity, we'll stick to 1 for now.
    """
    print("\nGenerating your story...")
    # The 'story_generator' is our loaded model.
    # We pass the user's 'prompt' to it.
    # 'max_length' controls how long the generated text can be.
    # 'num_return_sequences' allows for generating multiple options if desired.
    generated_texts = story_generator(
        prompt,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        # 'pad_token_id' helps the model know when to stop generating if it's shorter than max_length.
        # For GPT-2, it's often set to the end-of-sequence token id.
        pad_token_id=story_generator.tokenizer.eos_token_id
    )
    return generated_texts

# --- Part 5: Displaying the Story ---

def display_story(generated_texts):
    """
    Prints the generated story or stories to the console.
    """
    print("\n--- Your AI-Generated Story ---")
    if not generated_texts:
        print("No story was generated. Please try again with a different prompt.")
        return

    # We iterate through each generated text (even if there's only one).
    for i, story_output in enumerate(generated_texts):
        print(f"\nStory Option {i+1}:")
        # 'story_output' is a dictionary containing the generated text.
        # We access it using the key 'generated_text'.
        print(story_output['generated_text'])
        print("-" * 20) # Separator for multiple story options

# --- Part 6: Putting It All Together (Main Execution Block) ---

# This is the main part of our script that runs when you execute the file.
if __name__ == "__main__":
    # 1. Get the story idea from the user.
    user_prompt = get_user_prompt()

    # 2. Generate the story using the AI model.
    # We're asking for a story up to 150 words long.
    generated_story_options = generate_story(user_prompt, max_length=150)

    # 3. Show the generated story to the user.
    display_story(generated_story_options)

    print("\n--- End of Story Generator ---")

# --- Example Usage ---
#
# To run this code:
# 1. Save it as a Python file (e.g., story_generator.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python story_generator.py
#
# You will be prompted to enter a starting sentence.
#
# Example Interaction:
#
# Loading AI model... This may take a moment on the first run.
# Model loaded successfully!
#
# --- Let's start your story! ---
# Enter a sentence or a few words to start your story: The old wizard lived in a crumbling tower.
#
# Generating your story...
#
# --- Your AI-Generated Story ---
#
# Story Option 1:
# The old wizard lived in a crumbling tower. He was an old man, but he was strong. He was a man of the world, and he was a man of the people. He was a man of action, and he was a man of principle. He was a man of faith, and he was a man of hope. He was a man of peace, and he was a man of love. He was a man of mercy, and he was a man of grace. He was a man of truth, and he was a man of justice. He was a man of freedom, and he was a man of equality. He was a man of liberty, and he was a man of fraternity. He was a man of unity, and he was a man of peace. He was a man of love.
# --------------------
#
# --- End of Story Generator ---
#
# Another Example Prompt:
#
# Enter a sentence or a few words to start your story: A mysterious spaceship landed in the backyard.
#
# Generating your story...
#
# --- Your AI-Generated Story ---
#
# Story Option 1:
# A mysterious spaceship landed in the backyard. The aliens emerged from the ship and greeted the humans. The humans were scared, but they were also curious. The aliens told them that they were from a planet called Xylos, and that they had come to Earth to study the humans. The humans were amazed by the aliens, and they were also a little bit scared. The aliens told them that they were friendly, and that they had come in peace. The humans were relieved, and they were also a little bit excited. The aliens told them that they had come to Earth to learn about the humans, and that they had come to Earth to share their knowledge with the humans.
# --------------------
#
# --- End of Story Generator ---