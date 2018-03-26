import sys

def to_binary(n):
    return "{0:b}".format(n)

def base2palindrome(m):
    to_binary(m)

def main():
    m = int(sys.stdin.readline())
    print(base2palindrome(m))


if __name__ == "__main__": main()