#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.2.2 Observation 2-BubbleSort algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [-2, -55, -7, 14, -52, 29, -84, 62, 50, -59, 96, 54, 82, 41, -38, 88, 55, 37, -19, 4]
# added another array but it is commented out. it can be used to check whether the algoritm stops its sorting after it finds out the array is alreadt sorted
#array = [-84, -59, -55, -52, -38, -19, -7, -2, 4, 14, 29, 37, 41, 50, 54, 55, 62, 82, 88, 96]
numComparison = 0
numcopies = 0
#Displays the unsorted array created in the program
print("\nUnsorted Arrays: ", array)
numberElements = 20
#loops unitl it equals the numebr of elements in the array 
for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False 
                for j in range (numberElements-1):
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
    
