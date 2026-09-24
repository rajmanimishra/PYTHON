
#  reading mode

try:
   with open("data.txt","r") as file:
      print(file.read())
   
except FileNotFoundError:
      print("File exist nahi karti")


# writing mode
try:
    with open ("data.txt","w") as file:
        file.write("Here is the next lecture of it")
except FileNotFoundError:
        print(" file mil nahi rahi hai")

# try:
#    with open("data.txt","r") as file:
#       print(file.read())
   
# except FileNotFoundError:
#       print("File exist nahi karti")


# append the letters
with open ( "data.txt","a") as file:
    file.write("\n new characters are formed")

try:
   with open("data.txt","r") as file:
      print(file.read())
   
except FileNotFoundError:
      print("File exist nahi karti")


