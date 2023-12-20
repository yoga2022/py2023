## while
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations,you guessed it.')
        print('(but you do not win any prizes!)')

        running = False
    elif guess < number:
        print('No,it is a little higher than that')
    else:
        print('No,it is a little lower than that')
else:
    print('The while loop is over.')

print('Done')


## for
for i in range(1,5):
    print(i)

else:
    print("This for loop is over")

## break
while True:
    s = input("Enter something : ")
    if s == "quit":
        break
    print("length of the string is ",len(s))
print("Done")


## continue
while True:
    s = input("Enter something : ")
    if s == "quit":
        break
    if len(s) < 3:
        print("Too short")
        continue
    print("length of the string is ",len(s)) 
print("Done")