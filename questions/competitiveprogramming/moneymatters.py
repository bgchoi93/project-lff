import sys

class DisjointSet():
    def __init__(self, size):
        self.id = list(range(0,size))
        self.size = [1] * size
    def getRoot(self, i):
        while (i != self.id[i]):
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    def union(self, p, q):
        i = self.getRoot(p)
        j = self.getRoot(q)
        if (self.size[i] > self.size[j]):
            self.id[j] = i
            self.size[i] = self.size[j] + self.size[i]
        else:
            self.id[i] = j
            self.size[j] = self.size[j] + self.size[i]
        self.id[i] = j
    def find(self, p, q):
        return self.getRoot(p) == self.getRoot(q)

def moneymatter(balance, friendship):
     balancesheet = {}
     for i in range(0, len(balance)):
         root = friendship.getRoot(i)
         if root in balancesheet:
             balancesheet[root] = balancesheet[root] + balance[i]
         else:
             balancesheet[root] = balance[i]
     possible = True
     for key, value in balancesheet.items():
         if value != 0:
             return False
     return possible

def main():
    line = sys.stdin.readline()
    input = list(map(int, line.split(" ")))
    n = input[0]
    m = input[1]
    balance = {}
    for i in range(0,n):
        balance[i] = int(sys.stdin.readline())

    friendship = DisjointSet(n)
    for i in range(0,m):
        line = sys.stdin.readline()
        friends = list(map(int, line.split(" ")))
        friendship.union(friends[0], friends[1])
    if (moneymatter(balance, friendship)):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__": main()