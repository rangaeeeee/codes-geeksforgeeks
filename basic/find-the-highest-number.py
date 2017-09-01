'''


Find the Highest number
   
 
 

Given an array in such a way that the elements stored in array are in 
increasing order initially and then after reaching to a peak element , 
elements stored are in decreasing order. Find the highest element.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case consists of an integer n. 
The next line consists of n spaced integers. 

Output:
Print the highest number in the array.

Constraints: 
1<=T<=100
1<=n<=200
1<=a[i]<=105

Example:
Input:
2
11
1 2 3 4 5 6 5 4 3 2 1
9
1 3 4 5 7 8 9 5 2 

Output:
6
9

'''

testcase = int(input())

for i in range(testcase):
  number = int(input())
  print(max(list(map(int,input().split()))))