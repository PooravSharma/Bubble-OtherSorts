#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.3.2 Bi-directional-bubble sort (BDBS) algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [95, 100, 70, 98, -18, 20, -99, -43, 20, -30, 69, -40, -17, -37, 66, 24, -60, 96, -29, -23]

#added another array but it is commented out. it can be used to check whether the algoritm stops its sorting after it finds out the array is alreadt sorted
array = [-99, -60, -43, -40, -37, -30, -29, -23, -18, -17, 20, 20, 24, 66, 69, 70, 95, 96, 98, 100]

#worst case array (decending order)
array = [100, 98, 96, 95, 70, 69, 66, 24, 20, 20, -17, -18, -23, -29, -30, -37, -40, -43, -60, -99]

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
                for j in range (i, numberElements-1-i):
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
                for k in range (numberElements-2-i, i,-1):
                    #adds a count every time the elements are being compared
                    numComparison +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[k] < array[k-1]:
                       #add a count everytime the elements are being swapped
                        numcopies += 1
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = k-1
                        swap(array, k, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break;

#Displays the sorted array, number of comparison and copies(swaps)                      
print("\nSorted Array: ", array)
print(f"\nNumber of comparisons: {numComparison}")
print(f"\nNumber of copies(swaps): {numcopies}")
    
