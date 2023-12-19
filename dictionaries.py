# Define a function called word_frequency that takes a sentence as input
def word_frequency(sentence):
    # Split the sentence into a list of words
    words = sentence.split()  # Split the sentence into a list of words
    
    # Dictionary to store word frequencies
    frequency = {}  

    # Iterate through each word in the list of words
    for word in words:
        # If the word is already in the frequency dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # If the word is not in the frequency dictionary, add it with a count of 1
        else:
            frequency[word] = 1

    # Return the dictionary containing the frequency of each word
    return frequency

# Define a sentence
sentence = "This is a test sentence. This sentence is a test."

# Get the frequency of each word in the sentence using the word_frequency function
result = word_frequency(sentence)

# Print the dictionary containing word frequencies
print(result)
