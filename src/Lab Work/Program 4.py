import sys

# Program to count words in command line arguments

# Function to count words in a list of arguments
def word_count(args):
    count = 0
    for arg in args:
        count += len(arg.split())  # Split each argument into words and count them
    return count

# Main program execution
if __name__ == "__main__":
    count = word_count(sys.argv[1:])  # Exclude the script name from arguments
    print(f"Word count: {count}")