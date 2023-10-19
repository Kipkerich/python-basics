# Inbuilt functions
greeting = "Hello There"
print(greeting)
print(greeting.upper())
print(greeting.lower())


# Custom/User defined function
def motto():
    print("Hello there, this is our motto")


motto()
motto()


def add():
    x = 10
    y = 20
    z = x + y
    print("Your answer is", z)


add()


def addition(x, y, z):
    answer = x + y + z
    print("Your answer is", answer)


addition(300, 100, 500)
addition(20, 40, 40)


def avg(name, firstNumber, secondNumber, thirdNumber):
    answer = (firstNumber + secondNumber + thirdNumber) / 3
    print("Hello", name, "Your average is", answer)


avg("Jacob", 12, 36, 26)
avg("Kipkerich", 200, 400, 300)
avg("Jace", 30, 40, 20)


def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest
simple_interest(1000, 7, 5)
print(simple_interest(3000, 7 ,2))