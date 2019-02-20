'''
Write a task to judge if input year is leap year or not
'''
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

    return leap

year = int(input())
print(is_leap(year))