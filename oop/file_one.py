from our_classes_file import Fruit,Car,User,Admin
from abstraction import *

fruitOne = Fruit("Mango", "Yellow", "300g", 'Ksh.100')
fruitTwo = Fruit("Apple","Pink","250g","Ksh.70")

print(fruitOne.name)
print(fruitTwo.price)



carOne=Car("Mercedes","Grey","KCX298W","ksh.4,500,000")
carTwo=Car("Bugatti","Orange","KDN096W","ksh.105,000,000")
print(carTwo.price)

userOne = User("Jacob","jaykipkerich@gmail.com","jay@123")
userTwo = User("John","johndoe@gmail.com","john@123")

userOne.register()
userOne.login()

adminOne = Admin("Jay","jkipkerich@kabarak.ac.ke",'Jacob@123')

adminOne.login()
adminOne.suspendUsers()

toyotaOne=Toyota()
toyotaOne.mileage()

nissanOne=Gari()
nissanOne.mileage()