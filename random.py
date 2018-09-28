import random


x = int(raw_input("Please enter a number up to 100. "))
z = random.randint(40,100)

randomNumber = random.randint(1,z)
print "first random",randomNumber


if 35 >= randomNumber:
    newRandom = randomNumber * .5
    newRandom = newRandom + 9
    print "second random " "%.f" % newRandom

elif 36 <= randomNumber <= 93:
    newRandom = randomNumber + 7
    print "second random " "%.f" % newRandom

else:
    newRandom = randomNumber
    print "second random",newRandom