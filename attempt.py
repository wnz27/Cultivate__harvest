'''
@Author: 27
LastEditors: 27
@Date: 2020-05-08 01:55:10
LastEditTime: 2020-11-01 22:59:39
FilePath: /Coding-Daily/attempt.py
@description: type some description
'''
import random

a = random.sample(range(0, 200), 100)
print(a)

b = random.randint(0, 10)
print(b)

# assert 1 == 2, "1 不等于 2"
assert 1 == 1, "1 等于 1"

print([0] * 10)

for i in range(5, 0, -1):
    print(i)
