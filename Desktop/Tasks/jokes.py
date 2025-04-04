# Import the random module
import random

# Create a list of jokes with their punchlines
jokes = [
    {
        "setup": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    },
    {
        "setup": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "setup": "Why don't skeletons fight each other?",
        "punchline": "They don't have the guts."
    },
    {
        "setup": "What do you call fake spaghetti?",
        "punchline": "An impasta!"
    },
    {
        "setup": "Why did the bicycle fall over?",
        "punchline": "Because it was two-tired!"
    },
    {
        "setup": "What do you call cheese that isn't yours?",
        "punchline": "Nacho cheese!"
    },
    {
        "setup": "Why can't you give Elsa a balloon?",
        "punchline": "Because she will let it go!"
    }
]

# Select a random joke from the list
random_joke = random.choice(jokes)

# Display the joke and its punchline
print("Here's a random joke for you:")
print(random_joke["setup"])
print(random_joke["punchline"])