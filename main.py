import time
import matplotlib.pyplot as plt
import numpy as np

length = 30
unsortedList = np.random.randint(0,100,length)

n = len(unsortedList)
print(n)
x= np.arange(0,n, 1)



def bubbleSort(n, x, unsortedList, ax):
    copy = unsortedList.copy()
    for i in range (n):
        swaps = False
        for j in range(0,n-i-1):
            ax.bar(x, copy, color='red')
            ax.set_title("Bubble Sort", color= "white")
            plt.pause(0.00001)
            ax.clear()
            if copy[j]>copy[j+1]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
                swaps = True
        if swaps == False:
            return copy
            
    return copy

def insertionSort(n, x, unsortedList, ax):
    copy = unsortedList.copy()
    for i in range(1,n):
        keyVal= copy[i]
        j=i-1
        while j>=0 and keyVal<copy[j]:
            copy[j+1]=copy[j]
            j-=1
            ax.bar(x, copy, color='blue')
            ax.set_title("Insertion Sort", color= "white")
            plt.pause(0.00001)
            ax.clear()
            copy[j+1]=keyVal
    return copy


fig, (ax1, ax2) = plt.subplots(1,2, figsize =(10,5))
ax1.set_facecolor('black')
ax2.set_facecolor('black')
fig.patch.set_facecolor('black')


# Bubble Sort
start_time = time.time()
bubbleResult = bubbleSort(n, x, unsortedList, ax1)
bubbleTime = time.time() - start_time
ax1.bar(x, bubbleResult, color='red')
ax1.set_title(f"Bubble Sort Time for {n} items: {round(bubbleTime, 2)}s", color= "white")

# Insertion Sort
start_time = time.time()
insertionResult = insertionSort(n, x, unsortedList, ax2)
insertionTime = time.time() - start_time
ax2.bar(x, insertionResult, color='blue')
ax2.set_title(f"Insertion Sort for {n} items: {round(insertionTime, 2)}s", color= "white")

plt.show()