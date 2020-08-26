# TODO: Bubble Sort
def bubbleSort(numList):
    for n in range(len(numList)):
        for m in range(n + 1, len(numList)):
            # compared with (numList[n] > numList[n + 1])
            # the true bubble sort, compare between array[n] and array[n + 1]
            if numList[n] > numList[m]:
                numList[n], numList[m] = numList[m], numList[n]
        # print intermediate steps
        print("Real Time: ", numList)

    return numList

# TODO: the merge sort
# the divide-and-conquer algorithm
def 

# TODO: the 

# TODO: the quick sort

# TODO: use main in Python

def main():
    aTest = list([6,8,1,2,3,4,4])
    print(bubbleSort(aTest))

if __name__ == "__main__":
    main()

