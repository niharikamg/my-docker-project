import os

# Paths to input files
file1 = "IF.txt"
file2 = "AlwaysRememberUsThisWay.txt"

def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Count words in each file
count1 = word_count(file1)
count2 = word_count(file2)
total_count = count1 + count2

# Write results to a file
output_path = '/home/data/output/result.txt'
with open(output_path, 'w') as result_file:
    result_file.write(f"Word count of IF.txt: {count1}\n")
    result_file.write(f"Word count of AlwaysRememberUsThisWay.txt: {count2}\n")
    result_file.write(f"Total word count: {total_count}\n")

print("Results written to result.txt")
