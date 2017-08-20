'''

Pronic number is a number which is the product of two consecutive integers. 
The task is to check and print Pronic Numbers in a range. 
The first few Pronic numbers are:
0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132 and so on.

Input:
The first line consists of an integer T i.e number of test cases. 
The first and only line of each test case contains an integer n.

Output:
Print all the pronic numbers between 0 and n(with spaces in between).

Constraints: 
1<=T<=100
1<=n<=1000

Example:
Input:
2
6
56

Output:
0 2 6
0 2 6 12 20 30 42 56

'''

def printList(iList):
  for x in iList[:-1]:
    print(x,end=" ")
  print(iList[-1])

testcase = int(input())

for i in range(testcase):
  first = 0
  second = 1
  result = list()
  iLength = int(input())
  summation = first * second
  
  while(summation <= iLength):
    result.append(summation)
    first += 1
    second += 1
    summation = first * second
    
  printList(result)
