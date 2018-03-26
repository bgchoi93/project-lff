import sys
import math

def printer3d(n):
    # nunmber of printer grows exponentially until the printers are able to print all the statues
    return int(math.ceil(math.log2(n))) + 1

def main():
    n = int(sys.stdin.readline())
    print(printer3d(n))


if __name__ == "__main__": main()