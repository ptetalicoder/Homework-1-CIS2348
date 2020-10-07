#Pranav Tetali
#ID 1541822
#Homework 2 6.17


simplepassword=input()
password=''
for x in simplepassword:
    if(x=='i'):
        password+="!"          # can also be written as: password=password+"!"
    elif(x=='a'):
        password+="@"          # replaces a with @
    elif(x=='m'):
        password+="M"          # replaces m with M
    elif(x=='B'):
        password+="8"          # replaces B with 8
    elif(x=='o'):
        password+="."          # replaces o with .
    else:
        password+= x         # if the password does not have i,a,m,B,and o it returns to the original

password+="q*s"              # it adds q*s at the end
print("Stronger Password:")
print(password)
