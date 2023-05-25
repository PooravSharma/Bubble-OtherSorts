import random
import time

# Ask for a positive integer input and validate it
while True:
    num_elements = input("Enter the number of elements in the array: ")
    if num_elements.isnumeric() and int(num_elements) > 0:
        num_elements = int(num_elements)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

# Generate a random array of the given size
arr = [random.randint(-100, 100) for _ in range(num_elements)]

# Print the unsorted array
print("Unsorted array:", arr)

# Bubble sort the array and count the number of comparisons
num_comparisons = 0
start_time = time.time()
for i in range(num_elements - 1):
    for j in range(num_elements - i - 1):
        num_comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
end_time = time.time()

# Print the sorted array and the number of comparisons
print("Sorted array:", arr)
print(f"Number of comparisons: {num_comparisons}")

# Calculate the time it took to sort the array and print it in milliseconds
elapsed_time = (end_time - start_time) * 1000
print(f"Time taken: {elapsed_time:.2f} ms")
