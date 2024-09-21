from collections import Counter

# Program to find the most frequent words in a text file

# Function to find the most frequent words in a file
def most_frequent_words(filename):
    with open(filename, 'r') as file:
        text = file.read()  # Read the entire file content
    words = text.split()  # Split the text into words
    word_count = Counter(words)  # Count occurrences of each word
    most_common = word_count.most_common(5)  # Get the 5 most common words
    return most_common

# Example file name
filename = "/home/bjyotibrat/Programming/VS Code Programs/Jupyter Notebook/Lab Work/Input"

# Print the most frequent words
print("Most frequent words:")
print(most_frequent_words(filename))