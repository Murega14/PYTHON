#logical operators include and, or, not
#they are used to check if 2 or more conditional statements are true

temp = int(input("What is the temperature outside "))

if temp >=0 and temp <= 38:
    print("the temperature is good today!")
    print("you can go outside")

elif temp < 0 or temp > 30:
    print("bad temperatures today")
    print("please stay inside")

#if you wanted to reverse the conditions you can use the not operator before the arguments after the if or else
