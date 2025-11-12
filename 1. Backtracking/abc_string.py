import sys
from bisect import insort_left
def IO(name):
    if name:
        sys.stdin = open(name+'.inp', 'r')
        sys.stdout = open(name + '.out','w')

IO('')

input = lambda: sys.stdin.readline().strip()

class Sol:
    def __init__(self, n):
        self.n = n
        self.ans = []
        self.backtrack('')
        for r in self.ans:
            print(r)
    
    def backtrack(self, cur):
        if len(cur) == self.n:
            self.ans.append(cur)
            return

        if not cur:
            self.backtrack(cur+'A')
            self.backtrack(cur+'B')
            self.backtrack(cur+'C')
        elif cur[-1] == 'A':
            self.backtrack(cur+'B')
            self.backtrack(cur+'C')
        elif cur[-1] == 'B':
            self.backtrack(cur+'A')
            self.backtrack(cur+'C')
        elif cur[-1] == 'C':
            self.backtrack(cur+'B')
            self.backtrack(cur+'A')

def solve():
    Sol(int(input()))


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
