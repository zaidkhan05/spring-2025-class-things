#For the input sequence 10, 30, 26, 55, 11, 29 and hash function h(K) = K % 11,
#a. Construct the open hash table
#b. Find the largest number of key comparisons in a successful search in this table
#c. Find the average number of key comparisons in a successful search in this table
#d. Construct the closed hash table


def openHashTable(input_sequence):
    hash_table = [None] * 11  # Initialize the hash table with None
    for key in input_sequence:
        index = key % 11  # Hash function
        while hash_table[index] is not None:  # Handle collisions
            index = (index + 1) % 11
        hash_table[index] = key
    return hash_table

#largest num of key comparisons in a successful search
def largest_key_comparisons(hash_table):
    max_comparisons = 0
    for i in range(len(hash_table)):
        if hash_table[i] is not None:
            comparisons = 1
            index = (i + 1) % len(hash_table)
            while hash_table[index] is not None:
                comparisons += 1
                index = (index + 1) % len(hash_table)
            max_comparisons = max(max_comparisons, comparisons)
    return max_comparisons

#average num of key comparisons in a successful search
def average_key_comparisons(hash_table):
    total_comparisons = 0
    successful_searches = 0
    for i in range(len(hash_table)):
        if hash_table[i] is not None:
            comparisons = 1
            index = (i + 1) % len(hash_table)
            while hash_table[index] is not None:
                comparisons += 1
                index = (index + 1) % len(hash_table)
            total_comparisons += comparisons
            successful_searches += 1
    return total_comparisons / successful_searches if successful_searches > 0 else 0

#closed hash table
def closedHashTable(input_sequence):
    hash_table = [None] * 11  # Initialize the hash table with None
    for key in input_sequence:
        index = key % 11  # Hash function
        while hash_table[index] is not None:  # Handle collisions
            index = (index + 1) % 11
        hash_table[index] = key
    return hash_table



# input_sequence = [10, 30, 26, 55, 11, 29]
# hash_table = openHashTable(input_sequence)

# for index, value in enumerate(hash_table):
#     print(f"Index {index}: {value}")

# largest_comparisons = largest_key_comparisons(hash_table)
# print("Largest number of key comparisons in a successful search:", largest_comparisons)

# average_comparisons = average_key_comparisons(hash_table)
# print("Average number of key comparisons in a successful search:", average_comparisons)

# closed_hash_table = closedHashTable(input_sequence)
# print("Closed Hash Table:")
# for index, value in enumerate(closed_hash_table):
#     print(f"Index {index}: {value}")



# Construct a horspool table to calculate shift – 1.5 point
# • For the text ‘Ghosts make the best cheerleaders. They have lots of spirit!’
# • Pattern: best 

def horspool_table(pattern):
    table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - i - 1
    return table
#
# Example usage
pattern = "best"
text = "Ghosts make the best cheerleaders. They have lots of spirit!"
table = horspool_table(pattern)
print("Horspool table:")
for char, shift in table.items():
    print(f"Character: {char}, Shift: {shift}")
#

