#loop control statements changes a loops execution from its norrmal sequence
#break is used to terminate the loop entirely
#continue skips to the next iteration of the loop
#pass does nothing and acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "0741-644-151"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print()

for x in range(0, 21):
    if x == 13:
        pass
    else:
        print("{:d}".format(x), end="")