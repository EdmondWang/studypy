'''
Read an integer N.
Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.
'''
num = int(input())
print(*range(1, num + 1), sep = '')