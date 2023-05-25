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
#arr = [98, 93, 86, 84, 53, 52, 51, 48, 39, 24, 12, -1, -11, -23, -27, -39, -46, -66, -82, -88]
#arr = [24, 39, 48, 51, 52, 53, 84, 86, 93, 98, -88, -82, -66, -46, -39, -27, -23, -11, -1, 12]
# Print the unsorted array
print("Unsorted array:", arr)

# Cocktail sort the array and count the number of comparisons
num_comparisons = 0
start_time = time.time()
for i in range(num_elements // 2):
    # Set a flag to check if any swaps were made in the inner loop
    swapped = False
    # Move the largest element to the right
    for j in range(i, num_elements - i - 1):
        num_comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    # If no swaps were made in the inner loop, the array is already sorted
    if not swapped:
        break
    # Move the smallest element to the left
    for j in range(num_elements - i - 2, i , -1):
        num_comparisons += 1
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swapped = True
    # If no swaps were made in the inner loop, the array is already sorted
    if not swapped:
        break
end_time = time.time()

# Print the sorted array and the number of comparisons
print("Sorted array:", arr)
print(f"Number of comparisons: {num_comparisons}")

# Calculate the time it took to sort the array and print it in milliseconds
elapsed_time = (end_time - start_time) * 1000
print(f"Time taken: {elapsed_time:.2f} ms")
