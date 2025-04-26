
input = [10, 30, 26, 55, 11, 29]
hash_table = [None] * 11 # Initialize hash table with None values

for key in input:
    index = key % 11 # Hash function h(K) = K mod 11
    while hash_table[index] is not None: # Linear probing for collision resolution
        index = (index + 1) % 11
    hash_table[index] = key # Insert the key into the hash table

# Print the hash table
print("Open Hash Table:")

for i in range(len(hash_table)):
    if hash_table[i] is not None:
        print(f"Index {i}: {hash_table[i]}")
    else:
        print(f"Index {i}: None")

# The following code constructs an open hash table using linear probing for collision resolution.
# It also calculates the largest and average number of key comparisons in a successful search.














# For the input sequence 10, 30, 26, 55, 11, 29 and hash function h(K) = K mod 11,
# a. Construct the open hash table – 0.5 points
# b. Find the largest number of key comparisons in a successful search in this table – 0.5 points
# c. Find the average number of key comparisons in a successful search in this table – 0.5 points 