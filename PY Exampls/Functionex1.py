s_username="EMC"
s_password="123"

uname=input("Enter the username:")
pword=input("Enter the password:")

def validate():
    if(s_username==uname and s_password==pword):
        return True
    else:
        return False
    
a=validate()
print(a)

