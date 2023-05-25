#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.2.1 Observation 1-BubbleSort algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [86, -92, 77, 31, 83, -68, -50, 78, 37, 91, -15, -51, -57, -90, -12, 51, -37, -32, 8, -54]
numComparison = 0
numcopies = 0
#Displays the unsorted array created in the program
print("\nUnsorted Arrays: ", array)
numberElements = 20
#loops unitl it equals the numebr of elements in the array 
for i in range (numberElements):
                #as wanted in the observation 1 it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (numberElements-1-i):
                    #adds a count every time the elements are being compared
                    numComparison +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:
                       #add a count everytime the elements are being swaped
                        numcopies += 1
                        nextElement = j+1
                        swap(array, j, nextElement)

#Displays the sorted array, number of comparison and copies(swaps)                      
print("\nSorted Array: ", array)
print(f"\nNumber of comparisons: {numComparison}")
print(f"\nNumber of copies(swaps): {numcopies}")
    
