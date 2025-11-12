import sys, time
#from io import BytesIO
#from os import read, fstat
#from heapq import heapify, heappush, heappop
# from collections import defaultdict, deque, Counter, OrderedDict
#from math import gcd,log,log2,log10,sin,cos
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from typing import LiteralString
#from typing import List, Tuple
from functools import lru_cache, cmp_to_key

LOCAL = ''
def IO(name = ''):
    global LOCAL
    if name:
        LOCAL = name
        sys.stdin = open(name+'.inp', 'r')
        sys.stdout = open(name+'.out', 'w')

IO('')


input = lambda : sys.stdin.readline().strip()
#input = lambda : sys.stdin.buffer.readline().strip()
#input = BytesIO(read(0,fstat(0).st_size)).readline
#print = sys.stdout.write
# sys.setrecursionlimit(int(1e6))

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
        except SystemExit:
            end = time.time()
            if LOCAL:
                print(f"\n[Time taken: {end-start:.4f}s]", file = sys.stderr, flush = True)
            raise
        end = time.time()
        if LOCAL == 'task':
            print(f"\n[Time taken: {end-start:.4f}s]", file = sys.stderr, flush = True)
        return result
    return wrapper

# Constant
INF = 1<<60
MOD = int(1e9)+7
endl = '\n'


class Sol:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.a = list(map(int, input().split()))
        self.sum_arr = [0]*self.k
        self.idx_arr = [-1]*self.n
        if sum(self.a)%k != 0: print("ze"); return 

        self.backtrack(0)
        print("ze")

    def backtrack(self, cur):
        if cur == self.n: 
            if len(set(self.sum_arr)) == 1:
                print(*self.idx_arr)
                sys.exit()
            return
        
        for i in range(self.k):
            self.sum_arr[i] += self.a[cur]
            self.idx_arr[cur] = i+1
            self.backtrack(cur+1) 
            self.idx_arr[cur] = -1
            self.sum_arr[i] -= self.a[cur]

def solve():
    n,k = map(int, input().split())
    Sol(n,k)

@timed
def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
