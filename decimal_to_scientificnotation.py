number = input("Enter the number you want to convert: ")
sn = int(number)

text = "The number in scientific notation is: {:e}"
text2 =  "The number in scientific notation is: {:E}"

print(text.format(sn))
print(text2.format(sn))