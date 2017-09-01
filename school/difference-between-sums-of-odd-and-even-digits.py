T = int(input())
for t in range(0,T):
    N = list(map(int,str(int(input()))))
    if (sum(N[1::2]) - sum(N[0::2])) == 0:
      print("Yes")
    else:
      print("No")