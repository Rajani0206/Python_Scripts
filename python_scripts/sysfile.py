import random
import sys
import os

var=(random.randint(2, 10))
print("Random Number:", var)

print("Number range from 2 to 10")
for i in range (2,10):
    print(i)

print(sys.argv[0])

print(sys.argv[1])
print(sys.path)

print(os.getcwd())

os.makedirs("testdir1", exist_ok=True)

os.chdir("/home/ubuntu/testdir1")

print(os.getcwd())
