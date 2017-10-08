#Output only in one line
#Trying to make the output more... clear.
for x in range(1,101):
    if x % 3 == 0:
        print("Fizz", end=' ')
    elif x % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(x, end=' ')
