# CODE WITH HARRY

#_________________________________________________________
# day 10

# x = input("Enter 1st number :")
# y = input("Enter 2nd number :")
#
# print(x + y)
#
# print(int(x) + int(y))



#_________________________________________________________
# day 11

# string

# blog = '''so today,
#  we are going to have fun tonight
#  with office friends
#  we are going to to do party!!'''


# print(blog)
#
# for ch in blog:
#     print(ch)

#_________________________________________________________
# day 12
#
# fruit = "mango"
# print(len(fruit))
#
# # print(fruit[0:4])
# # print(fruit[0:1])
# # print(fruit[:5])
# print(fruit[-3])

# name = "harry"
# print(name[-4:-2])

#_________________________________________________________
#Day 13

# a = "HrusHi kharade"
# name = "Hrushi**!!!"
# print(len(a))
# a1 = a.upper()        # Strings are immutable
# print(a1)
# print(a)
# a2 = a.lower()
# # print(a2)
# print(name.rstrip("!"))

# print(name.replace("Hrushi","Gaurav"))

# print(a.split(" "))

# print(a.count("H"))

# str1 = "WelcomeTotheJungleboyzzz99"

# print(str1.isalnum())

# str2 = "HowareYouMitroo"

# print(str2.isalpha())

#_________________________________________________________


# DAY 18 --         IF-ELSE STATEMENTS------------

# age = int(input("Enter Your Age:"))
# print("Your Age is: ",age)

# if(age>18):
#     print("you can drive")
# else:
#     print("You cannot drive!!!!!!!")

#_________________________________________________________


# applePrice = 300
# budget = int(input("whats your budget??"))

# if(applePrice<=budget):
#     print("jarvis, add apples to Cart")
# else:
#     print("Your budgget is low!")

#_________________________________________________________
#  elif condition

# number = int(input("Enter the number: "))

# if(number < 0):
#     print("value is negative")
# elif(number == 0):
#     print("value is neutral as ZERO")
# elif(number==50):
#     print("this is special value!!!!!!!!!!woahhh")    
# else:
#     print("value is positive")

#_________________________________________________________
# NESTED if

# number1 = int(input("Enter the number"))

# if(number1 < 0):
#     print("value is negative")
# elif(number1 > 0):
#     if (number1 > 0 and number1 <=20):
#         print("value is between 0-20")
#     elif(number1 > 20 and number1<30):
#         print("value lies between 20-30")
#     else:
#         print("greatest value of all time")
# else:
#     print("number is zero")

#_________________________________________________________

# EXERCISE CODE WITH HARRY PROBLEM STATEMENT....................

# import time

# time1 = time.strftime("%H:%M:%S")
# timestamp = int(time.strftime("%H"))
# print(time1)
# print(timestamp)
# timestamp1 = 10

# if (timestamp<0):
#     print("Good night")
# elif(timestamp>=12):
#     if(timestamp>=12 and timestamp < 16):
#         print("Good afternoon")
#     else:
#         print("Good evening")
# else:
#     print("Good morning")


#_________________________________________________________


# Day 16 match case


#_________________________________________________________


# DAY 17 --- FOR LOOP

# name = "Hrushikesh"
# for i in name:
#     print(i)

# ----------------------


# name = "Hrushikesh"
# for i in name:
#     print(i)
#     if (i=="s"):
#         print("special character found at this place!")

# ----------------------------

# colors = ['red','blue','green','white','pink', 'yellow']

# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
# -------------------------------
# RANGE ()-----------
# p = int(input('ENter the numner'))
# for i in range(p):
#     print(i+1)

# ---------------------------------
# for k in range(3,12):
#     print(k)   # it will give all the numbers for 3 to 12-1 =11  
# --------------------------

# for k in range(1,20,4):
#     print(k)   # here when we gave 4 at that time it gives output 1,5,9,13,17 coz it skips 4 numbers from 1 and gave 5 so on. (start,stop,step)

# ----------------------------------------

# DAY 18 -- WHILE LOOP\\

# i = 1 
# while (i<=5):
#     print(i)
#     i = i+1

# ---------------------------------

# count = 5
# while(count>0):
#     print(count)
#     count = count -1

# -------------------------------------

# DAY 19 BREAK AND CONTINUE

# break 

# for i in range(15):
#     if (i==10):
#         print("loop is breaked here!!")
#         break
#     print("2 X", i+1,"=", 2*(i+1))

# -------------------------------------
# continue

# for i in range(15):
#     if(i==10):
#         print("skip this part")
#         continue
#     print("9 X",i,"=", 9*(i))

# -------------------------------------
# DAY 20 ----- FUNCTIONS

# -------------------------------------

# def calculateAdd(a, b):
#     add = a + b
#     print(add)

# def greater(a, b):    
#     if (a >b):
#         print("1st number is greater then 2nd")
#     else:
#         print("2nd number is greater than  1st")

# a = 50
# b = 80
# greater(a,b)
# calculateAdd(a,b)

# c = 30700
# d = 9877
# greater(c,d)
# calculateAdd(c,d)

# calculateAdd(40,60)
# greater(40,60)

# -------------------------------------

# DAY 21 ---- FUNCTIONS ARGUMENTS AND RETURN STATEMENT

# def average(a,b):  # Required argument
#     print("average is :",(a+b)/2)

# average(6,4)

# ------------------------------
# def name(fname, mname, lname):
#     print("Full name is:",fname,mname,lname)

# name("Hrushikesh","bharat","Kharade")

# ---------------------------------------
# def average(*numbers): ____________________ # AS TUPLE
#     sum = 0
#     for i in numbers:
#         sum = sum + i 
#     print("The average is :", sum /len(numbers))

# average(50,23,56,78,65,333)

# ----------------------------
# def name(**name):  #___________________________________________as dictionary
#     print("Hello!",name['fname'],name['mname'],name['lname'])

# name(mname='bharat',lname='kharade',fname='hrushikesh')

# _----------------------------------------------

# DAY 22 ---- LIST

# marks = [45,87,90,88,56]

# s = sum(marks)
# print(marks)
# print(s/len(marks))

# # =-------------------------


