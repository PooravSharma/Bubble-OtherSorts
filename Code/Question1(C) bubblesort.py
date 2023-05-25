#method to swap the elements if the current element is bigger than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    
print("Question 1.1 Bubble sort algorithm")
#decided input he the elements on the array myself. the array contains 20 elements. 
array = [-89, 25, 57, 17, 44, -34, 61, 20, -48, 98, -30, -80, -93, -21, -7, -96, -66, -67, -71, -68]
numComparison = 0
numcopies = 0
#Displays the unsorted array created in the program
print("\nUnsorted Arrays: ", array)
numberElements = 20
#loops unitl it equals the numebr of elements in the array 
for i in range (numberElements):
                for j in range (numberElements-1):
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
    
