# Function to print dictionary values given the keys:
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # Changed dictionery [k] to dictionery [key] 

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd\'oh!', # Fixed the apostrophe in "d'oh!" by escaping it
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # Changed the function call to pass a list of keys ['lisa', 'bart', 'homer'] instead of individual strings

# Expected console output:
# BAAAAAART!
# Eat My Shorts!
# d'oh!