import random
import math
import argparse

def createArray(min, max, size):
    print("Initializing the input array...\nMax integer value: {}\nMin integer value: {}\nArray size: {}".format(max, min, size))
    A = []
    for i in range(0, size):
        n = random.randint(min, max)
        A.append(n)
    print("Input array: {}".format(A))
    return A

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def findMax(A, n):
    if n == 0:
        return A
    else:
        maxA = -math.inf
        for i in range(0, n+1):
            if A[i] >= maxA:
                maxA = A[i]
                largest = i
        swapPositions(A, largest, n)
        return findMax(A, n-1)


if __name__ == "__main__":
    # initialize a parser
    parser = argparse.ArgumentParser()

    # add args to the parser
    parser.add_argument("-m", "--min", type=int, help="minimum value allowed for the integer array")
    parser.add_argument("-M", "--max", type=int, help="maximum value allowed for the integer array")
    parser.add_argument("-s", "--sample-size", dest="size", type=int, help="size of the input array")

    # parse the arguments
    args = parser.parse_args()

    # create and sort the array
    A = createArray(args.min, args.max, args.size)
    print("About to sort the array...")
    A = findMax(A, len(A)-1)
    print("Sort complete.\nPartitioned array: {}".format(A))
