import sys
from datetime import datetime
import time

def calculate_time_until_explosion(now_str, explosion_str):
    now = datetime.strptime(now_str, "%H:%M:%S")
    explosion = datetime.strptime(explosion_str, "%H:%M:%S")

    difference = explosion - now

    if difference.seconds == 0:
        return "24:00:00"
    else:
        return time.strftime("%H:%M:%S", time.gmtime(difference.seconds))

def main():
    now = sys.stdin.readline().replace("\n", "")
    explosion = sys.stdin.readline().replace("\n", "")
    print(calculate_time_until_explosion(now, explosion))


if __name__ == "__main__": main()
