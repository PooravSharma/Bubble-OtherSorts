import time
import random

#method to swap the elements if the current element is bigger or smaller than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
#a method to generate a array with random element ranging from -2000 to 2000    
def randomElements(elementNumber):
     array = [random.randint(-2000, 2000) for i in range(elementNumber)]
     return array
 #method displays the options that the user can pick from    
def optionDisplay(displayNumber):     
    if displayNumber == 1:
        print("\n1. Test an individual sorting algorithm\n")
        print("2. Test multiple sorting algorithms\n")
        print("3. Exit\n")
    else:
        print("\nSelect the sorting algorithm to test\n")
        print("1. Test selection sort algorithm\n")
        print("2. Test insertion sort algorithm\n")
        print("3. Test merge sort algorithm\n")
        print("4. Test quick sort algorithm\n")
        print("5. Test heap sort algorithm\n")
        print("6. Test bubble sort algorithm\n")
        print("7. Test Obs1-bubble sort algorithm\n")
        print("8. Test Obs2-bubble sort algorithm\n")
        print("9. Test Obs3-bubble sort algorithm\n")
        print("10. Test Sink-down sort algorithm\n")
        print("11. Test Bi-directional sort algorithm\n")
        print("12. Exit\n")
#this method accepts only valid integer which can be used choose an option  
def optionInput(max, min, displayNumber):
    optionDisplay(displayNumber)
    while True:
        optionNumber = input("\nEnter number to choose option: ")
        if optionNumber.isnumeric() and max > int(optionNumber) > min:
            optionNumber = int(optionNumber)
            break
        else:
            print("\nError!!! Invalid Input \nPlease insert correct option number\n")
            optionDisplay(displayNumber)
    return optionNumber

 #askes the user to input a integer that can be used as the number of element in the array   
def numberofElement():
    while True:
        elementNumber = input("\nEnter number to element you want in the array: ")
        if elementNumber.isnumeric() and int(elementNumber) > 0:
            elementNumber = int(elementNumber)
            break
        else:
            print("\nError!!! Invalid Input \nPlease insert an integer more than 0.\n")
            firstOptionDisplay()
    return int(elementNumber)
#this method deals with the option that the users has chosen    
def chosenOption(optionNumber):
    if optionNumber == 1:
        secondOption(optionInput(13, 0, 0))
    elif optionNumber == 2:
        testMultipleAlgorithms();
    else:
        print("\nExiting\n")
        exit()
#it shows the first option of testing individual sorthing algorithm. it display the number of comparison and its run time. 
def secondOption(optionNumber):
    
    if optionNumber ==12:
        print("\nExiting\n")
        exit()
        
    array = randomElements(numberofElement())
    print("Unsorted Array: ", array)
    
    if optionNumber ==1:
        print("\nTesting selection sort algorithm\n")        
        result = selectionSort(array)
        
    elif optionNumber ==2:
        print("\nTesting insertion sort algorithm\n")
        result = insertionSort(array)
        
    elif optionNumber ==3:
        print("\nTesting merge sort algorithm\n")        
        result = mergeSort(array)
        
    elif optionNumber ==4:
        print("\nTesting quick sort algorithm\n")
        result = quickSort(array)
        
    elif optionNumber ==5:
        print("\nTesting heap sort algorithm\n")
        result = heapSort(array)
        
    elif optionNumber ==6:
        print("\nTesting bubble sort algorithm\n")
        result = bubbleSort(array)
        
    elif optionNumber ==7:
        print("\nTesting Obs1-bubble sort algorithm\n")
        result = obs1bubbleSort(array)
        
    elif optionNumber ==8:
        print("\nTesting Obs2-bubble sort algorithm\n")
        result = obs2bubbleSort(array)
        
    elif optionNumber ==9:
        print("\nTesting Obs3-bubble sort algorithm\n")
        result = obs3bubbleSort(array)
    elif optionNumber ==10:
        print("\nTesting Sink-down sort algorithm\n")
        result = sinkdownSort(array)
    elif optionNumber ==11:
        print("\nTesting Bi-directional sort algorithm\n")
        result = bidirectionalSort(array)
       
    print(f"Sorted Array: ", result[2])
    print(f"\nRun time (ms): ", result[0])
    print(f"Number of Comparisons: ", result[1])

#made a lot of variables because the code was showing some issues. i have since fixed the code and everything is runing smoothly
def testMultipleAlgorithms():
    print("Testing Multiple Sorting Algorithms")
    array = randomElements(numberofElement())
    print("Unsorted Array: ", array)
    arr1 = array.copy()
    arr2 = array.copy()
    arr3 = array.copy()
    arr4 = array.copy()
    arr5 = array.copy()
    arr6 = array.copy()
    arr7 = array.copy()
    arr8 = array.copy()
    arr9 = array.copy()
    arr10 = array.copy()
    arr11 = array.copy()
    
    resulta = selectionSort(arr1)
    resultb = insertionSort(arr2)
    resultc = mergeSort(arr3)
    resultd = quickSort(arr4)
    resulte = heapSort(arr5)
    resultf = bubbleSort(arr6)
    resultg = obs1bubbleSort(arr7)
    resulth = obs2bubbleSort(arr8)
    resulti = obs3bubbleSort(arr9)
    resultj = sinkdownSort(arr10)
    resultk = bidirectionalSort(arr11)
    
    row1 = ['Selection Sort', len(array), resulta[1], resulta[0]]
    row2 = ['Insertion Sort', len(array), resultb[1], resultb[0]]
    row3 = ['Merge Sort', len(array), resultc[1], resultc[0]]
    row4 = ['Quick Sort', len(array), resultd[1], resultd[0]]
    row5 = ['Heap Sort', len(array), resulte[1], resulte[0]]
    row6 = ['Bubble Sort', len(array), resultf[1], resultf[0]]
    row7 = ['Obs1-Bubble Sort', len(array), resultg[1], resultg[0]]
    row8 = ['Obs2-Bubble Sort', len(array), resulth[1], resulth[0]]
    row9 = ['Obs3-Bubble Sort', len(array), resulti[1], resulti[0]]
    row10 = ['Sink-Down Sort', len(array), resultj[1], resultj[0]]
    row11 = ['Bi-Directional Sort', len(array), resultk[1], resultk[0]]  
      
   
    
    print("\nSorted Array: (descending order) ", resultj[2])
    print("\nSorted Array: (ascending order)", resultk[2])

    resultTable = [
                ['Sorting Algorithm Name', 'Array Size', 'Number of Comparisons', 'Run Time(in ms)'],
                 row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11
                  ]

    #checking and setting the length of the coloum to the maximum length of the row.     
    coloumLength = []
    for i in range (len(resultTable[0])):
        maxLength = max(len(str(row[i])) for row in resultTable)
        coloumLength.append(maxLength)
    #uses to create the border of the table
    border = '-' + '---'.join('-' * length for length in coloumLength) + '-----'
    #the code below is used to display the rows from the result table
    rows = ''
    for row in resultTable:
        row_string = '| '
        for i in range(len(row)):
            if i == 0:
                               #this code is used to set the alignment of the data (this was is for left align)
                row_string += '{:<{}}'.format(row[i], coloumLength[i])
            else:               #this code is used to set the alignment of the data (this was is for center align)
                row_string += ' | {:^{}}'.format(str(row[i]), coloumLength[i])
            row_string += ' '
        row_string += '|'
        rows += row_string + '\n'
        rows += border + '\n'
   #these codes display the table 
    print(border)
    print(rows.strip())

#these following 5 sorting algorithms were made thanks to the lesson 4 and 7 in canvas    
def selectionSort(array):   
    elementNumber = len(array)
    numberofComparisons = 0
    startClock = time.time()
    for i in range(elementNumber):
        minimumIndex = i;
        for j in range(i+1, elementNumber):
            numberofComparisons +=1
            if array[j]<array[minimumIndex]:
                minimumIndex = j
        swap(array, i, minimumIndex)
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def insertionSort(array):
    elementNumber = len(array)
    numberofComparisons = 0
    startClock = time.time()
    for i in range(1, elementNumber):
        key = array[i]
        j = i-1
        while j>=0:
            numberofComparisons +=1
            if array[j]>key:
                array[j+1] = array[j]
                j-=1
            else:                
                break            
        array[j+1] = key        
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array
#referenced lesson 4 powerpoint
def mergeSort(array):
    elementNumber = len(array)
    numberofComparisons = 0
    startClock = time.time()    
    sortedArray = [None]*elementNumber
    numberofComparisons += mergeSortHelper(array, sortedArray, 0, elementNumber-1)
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array
    
def mergeSortHelper(array, sortedArray, low, high):
    elementNumber = len(array)
    numberofComparisons = 0
    if low < high:
        middle = (high+low)//2
        numberofComparisons += mergeSortHelper(array, sortedArray, low, middle)
        numberofComparisons += mergeSortHelper(array, sortedArray, middle+1, high)
        numberofComparisons += merge(array, sortedArray, low, middle, high)
    return numberofComparisons

def merge(array, sortedArray, low, middle, high):    
    i1 = low
    i2 = middle+1
    numberofComparisons = 0
    for i in range(low, high+1):
        if i1>middle:
            sortedArray[i]=array[i2] 
            i2 +=1
        elif i2>high:
            sortedArray[i] = array[i1] 
            i1 +=1
        elif array[i1]<array[i2]:
            numberofComparisons +=1
            sortedArray[i] = array[i1] 
            i1 +=1            
        else:                 
            numberofComparisons +=1
            sortedArray[i] = array[i2] 
            i2 +=1
    for i in range(low, high+1):            
        array[i] = sortedArray[i]     
    return numberofComparisons
#referenced lesson 4 powerpoint

def quickSort(array):
    numberofComparisons = 0
    startClock = time.time()    
    numberofComparisons += quicksortHelper(array, 0, len(array) - 1)
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array
def quicksortHelper(array, left, right):
    numberofComparisons = 0
    if left < right:
        pivotLocation, numberofComparisons = partition(array, left, right)
        numberofComparisons += quicksortHelper(array, left, pivotLocation - 1)
        numberofComparisons += quicksortHelper(array, pivotLocation + 1, right)
    return numberofComparisons

def partition(array, left, right):
    numberofComparisons = 0
    middle = (left + right) // 2
    pivot = array[middle]
    array[middle] = array[right]
    array[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        numberofComparisons += 1
        if array[index] < pivot:
            swap(array, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (array, right, boundary)
    return boundary, numberofComparisons

def heapSort(array):
    numberofComparisons = 0
    startClock = time.time()       
    
    #print(range(len(array)-1, -1, -1))
    #(1) Build a heap based on the elements in array[ ];
    for i in range(len(array)-1, -1, -1):
        Heap(array, len(array), i)
    #(2) for i = n-1 down to 1
    for i in range(len(array)-1, 0, -1):
        #swap the element at root with the element in position i;
        array[i], array[0] = array[0], array[i]
        #restore the heap property for sub-array[0, …, i-1];
        numberofComparisons +=Heap(array, i, 0)
        
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def Heap(array, length, index):
    #build a heap with root at array [index], and heap nodes in array[index...length]
    #Assuming that the two children of node array[index] are heaps already.
    numberofComparisons = 0
    larger_index = index
    l_child = 2 * larger_index + 1
    r_child = 2 * larger_index + 2
    numberofComparisons += 1
    if l_child < length and array[larger_index] < array[l_child]:
        larger_index = l_child
    numberofComparisons += 1
    if r_child < length and array[larger_index] < array[r_child]:
        larger_index = r_child
    numberofComparisons += 1
    if larger_index != index:
        array[index], array[larger_index] = array[larger_index], array[index]

        numberofComparisons +=Heap(array, length, larger_index)
    return numberofComparisons
    
def bubbleSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time()  
    for i in range (numberElements):
                for j in range (numberElements-1):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                    #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:                                            
                        nextElement = j+1
                        swap(array, j, nextElement)
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def obs1bubbleSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time() 
    for i in range (numberElements):
                #as wanted in the observation 1 it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (numberElements-1-i):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:                     
                        nextElement = j+1
                        swap(array, j, nextElement)
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def obs2bubbleSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time() 
    for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False 
                for j in range (numberElements-1):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:          
                        swapped = True #sets a swapped boolean as True because the elements are being swaped
                        nextElement = j+1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def obs3bubbleSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time() 
    for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False
                #it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (numberElements-1-i):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:                                           
                        swapped = True  #sets a swapped boolean as True because the elements are being swaped
                        nextElement = j+1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def sinkdownSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time() 
    for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False
                #it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (numberElements-1, i, -1):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j-1]:
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = j-1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array

def bidirectionalSort(array):
    numberofComparisons = 0
    numberElements = len(array)
    startClock = time.time()
    for i in range (numberElements):
                #sets a swapped boolean as false becasue no swaps have been made yet
                swapped = False
                #it reduces the number of comparisons to be made by reducing the number of iteration. It is reduced by the number of outer loop that has occured and - 1 for the first iteration. 
                for j in range (i, numberElements-1-i):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[j] > array[j+1]:
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = j+1
                        swap(array, j, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break
                for k in range (numberElements-2-i, i,-1):
                    #adds a count every time the elements are being compared
                    numberofComparisons +=1
                     #comapares the elements to see if the curent element is bigger than the next one or not
                    if array[k] < array[k-1]:
                         #sets a swapped boolean as True because the elements are being swaped
                        swapped = True 
                        nextElement = k-1
                        swap(array, k, nextElement)
                #Breaks away from the loop and ends the sorting process no element were swapped = array is already sorted
                if not swapped:
                    break
    endClock = time.time()
    runTime = (endClock - startClock)*1000
    return runTime, numberofComparisons, array
#the code below is what would normally be in a main ().

print("Question 3 Testing Various Cases of Sorting algorithm\n")
looping = True
while looping == True:
    chosenOption(optionInput(4, 0, 1))

