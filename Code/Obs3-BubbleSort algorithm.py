#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.2.3 Observation 3-BubbleSort algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [-94, -92, 15, 37, 62, 77, -87, -34, 83, 96, -73, 18, -95, -2, -7, 28, 59, 53, 46, 61]

#added another array but it is commented out. it can be used to check whether the algoritm stops its sorting after it finds out the array is alreadt sorted
#array = [-95, -94, -92, -87, -73, -34, -7, -2, 15, 18, 28, 37, 46, 53, 59, 61, 62, 77, 83, 96]

#worst case array (decending order)
#array = [96, 83, 77, 62, 61, 59, 53, 46, 37, 28, 18, 15, -2, -7, -34, -73, -87, -92, -94, -95]

numComparison = 0
numcopies = 0
#Displays the unsorted array created in the program
print("\nUnsorted Arrays: ", array)
numberElements = 20
#loops unitl it equals the numebr of elements in the array 
for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False
                #it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (numberElements-1-i):
                    #adds a count every time the elements are being compared
                    numComparison +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:
                       #add a count everytime the elements are being swapped
                        numcopies += 1
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = j+1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break;

#Displays the sorted array, number of comparison and copies(swaps)                      
print("\nSorted Array: ", array)
print(f"\nNumber of comparisons: {numComparison}")
print(f"\nNumber of copies(swaps): {numcopies}")
    
