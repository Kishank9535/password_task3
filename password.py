import random
ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()._"
while 1:
    p_length=int(input("Enter the lenght for the password to be generated : "))
    p_count=int(input("How many password to be generated : "))
    for i in range(0,p_count):
       password=""
       for j in range(0,p_length):
           a=random.choice(ch)
           password=password + a
       print("Here is your Passwords : ",password)    