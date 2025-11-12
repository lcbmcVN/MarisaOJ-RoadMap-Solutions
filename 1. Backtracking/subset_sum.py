import sys
from bisect import insort_left
def IO(name):
    if name:
        sys.stdin = open(name+'.inp', 'r')
        sys.stdout = open(name + '.out','w')

IO('')

input = lambda: sys.stdin.readline().strip()

class Sol:
    def __init__(self, n, target, a):
        self.n = n
        self.target = target
        self.a = a

        self.backtrack(0,0)
        print("NO")

    
    def backtrack(self, idx,  cur):
        if cur > self.target: return
        if cur == self.target:
            print("YES")
            sys.exit()

        for i in range(idx, self.n):
            self.backtrack(i+1, cur+self.a[i])

def solve():
    n,target = map(int, input().split())
    a = list(map(int, input().split()))
    Sol(n,target,a)

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
