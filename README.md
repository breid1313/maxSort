# Overview

This is an example of a recursive solution to sort an array of integers in ascending order.
The input is an array of randomly generated integers and the output is the same array with key values increasing with array indices.
That is, the values of the array increase from left to right.

# Usage
Since this program depends on the `math.inf` functionality, only Python3 is supported.
Three arguments are required to run the program: `--min (-m)`, `--max (-M)`, and 
`--sample-size (-s)`. These arguments affect the composition of the input array that will be partitioned.
The `--min` argument sets the minimum allowed value of an integer in the array, the `--max` argument sets the maximum
allowed value of an integer in the array, and the `--sample-size` argument sets the size of the array that will be generated.
You may provide the arguments in any order.

The following will generate and sort a 20-element array composed of integers ranging from 0 to 100:

`python3 maxSort.py -m 0 -M 100 -s 20`

Happy sorting!