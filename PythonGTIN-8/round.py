import math
def round():
    sum = int(input())
    if (sum % 10):
        sum = sum + (10 - sum % 10)
        print(sum)

round()
