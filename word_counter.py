def count_words_in_file(file_path, search_words):
    # Initialize a dictionary to store the count of each word in search_words
    word_count = {word: 0 for word in search_words}

    try:
        print(f"Opening file: {file_path}")  # Debug print
        # Open the file and read each line
        with open(file_path, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace
                word = line.strip()
                print(f"Read word: {word}")  # Debug print
                if word in word_count:
                    word_count[word] += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return word_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return word_count

    return word_count

# Define the list of search words (case-sensitive)
search_words = ["Python", "C", "OOP", "Hello", "Java"]

# Define the path to the input file
file_path = 'input.txt'  # Use relative path since input.txt is in the same directory as word_counter.py

# Get the word counts
word_counts = count_words_in_file(file_path, search_words)

# Print the results
for word, count in word_counts.items():
    print(f"{word} -> {count}")
