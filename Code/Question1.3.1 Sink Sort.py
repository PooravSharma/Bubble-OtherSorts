#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.3.1 SinkSort algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [51, -39, -88, 39, -1, 98, -46, -27, 84, -82, 52, -23, 53, -66, 93, 12, -11, 86, 48, 24]

#added another array but it is commented out. it can be used to check whether the algoritm stops its sorting after it finds out the array is alreadt sorted
#array = [98, 93, 86, 84, 53, 52, 51, 48, 39, 24, 12, -1, -11, -23, -27, -39, -46, -66, -82, -88]

#worst case array (ascending order)
#array = [-88, -82, -66, -46, -39, -27, -23, -11, -1, 12, 24, 39, 48, 51, 52, 53, 84, 86, 93, 98]


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
                for j in range (numberElements-1, i, -1):
                    #adds a count every time the elements are being compared
                    numComparison +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j-1]:
                       #add a count everytime the elements are being swapped
                        numcopies += 1
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = j-1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break;

#Displays the sorted array, number of comparison and copies(swaps)                      
print("\nSorted Array: ", array)
print(f"\nNumber of comparisons: {numComparison}")
print(f"\nNumber of copies(swaps): {numcopies}")
    
