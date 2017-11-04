#Manage Inpunts
ocupation =input("What is your ocuppation?")
city=input("What city do you live in?")
age=input("How many years old are you?")

name="simon"
length=len(name)

num=9
string=str(num)

#prints "so you are a [ocupation],you live[city], and you are[age] years old"
print("So you are a %s, you live %s, and you are %s years old" %(ocupation,city,age))
print("The word 'simon' has %s characteres" % (length))
print("this is a number",num)
print("but this is a number converted to string %s with 'str()'" %(string))

#upercase and lowercase
str1="LOWER"
str2="upper"
print(str1)
print(str1.lower())
print(str2)
print(str2.upper())