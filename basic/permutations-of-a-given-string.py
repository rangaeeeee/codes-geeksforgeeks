'''
Permutations of a given string

Given a string, print all permutations of a given string.

Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case contains a single string in capital letter.

Output:

Print all permutations of a given string with single space and all permutations
should be in lexicographically increasing order.

Constraints:

1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:

Input:
2
ABC

ABSG

Output:
ABC ACB BAC BCA CAB CBA

ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS
GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA 

'''

from itertools import permutations

def printList(iList):
  for x in iList[:-1]:
    print(x,end=" ")
  print(iList[-1])


def joinTuple(inputTuple):
  '''
  join the two dimensional list
  ('A', 'B', 'C') ('A', 'C', 'B') to (ABC) (ACB)
  '''
  result = list()
  for x in inputTuple:
      result.append(''.join(x))
  return result

testcase = int(input())

for i in range(testcase):
  string = input()
  result = (permutations(sorted(string),len(string)))
  output = joinTuple(result)
  printList(output)
  
