income=int(input("Enter your Income:"))
Name=input("Name:")
Age=int(input("Enter the Age:"))
if(income<20000):
    print("Loan is not Available")
elif(income>=50000 or Age<=25):
    print("Loan is available")
else:
    print("Loan is not available")

          
