#Output only in one line thks to "end=" :D
#Doesnt work on version 2 :( just remove the "end=' '"
for x in range(1,100):
    if x%3==0:
        print("Fizz", end=' ')
    elif x%5==0:
        print("Buzz", end=' ')
    else:
        print(x, end=' ')
