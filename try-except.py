try:
 n=int (input("Enter the 1st number : "))
 m=int (input("Enter the 2nd number : "))
 result=n/m
 print((result))
 
except ValueError:
    print("number hi enter karo")
except ZeroDivisionError:
    print("zero se divide nahi kar sakte")
    
finally:
    print("This will run in every case")