text = "Hello there i'm really enjoying python\n"
with open('text.txt','w') as file:
    file.write(text)

#say you want another text that accepts input
user = input("enter a text: ")
with open('text.txt','a') as file: #notice i've used a for append
    file.write(user)