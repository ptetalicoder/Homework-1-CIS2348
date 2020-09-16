# Pranav Tetali
#ID#1541822


#1
lemonjuice=float(input("Enter amount of lemon juice (in cups):\n"))
water=float(input("Enter amount of water (in cups):\n"))
agavenectar=float(input("Enter amount of agave nectar (in cups):\n"))
serving=float(input("How many servings does this make?\n"))

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(serving))+' servings')
print(str('{:.2f}'.format(lemonjuice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(water))+' cup(s) water')
print(str('{:.2f}'.format(agavenectar))+' cup(s) agave nectar\n')

#2
newserving=float(input("How many servings would you like to make?\n"))
s=newserving/serving
newlemonjuice=lemonjuice
newwater=water*s
newagavenectar=agavenectar*s

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(newserving))+' servings')
print(str('{:.2f}'.format(newlemonjuice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(newwater))+' cup(s) water')
print(str('{:.2f}'.format(newagavenectar))+' cup(s) agave nectar')

#3
print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(newserving))+' servings')
print(str('{:.2f}'.format(newlemonjuice/16))+' cup(s) lemon juice')
print(str('{:.2f}'.format(newwater/16))+' cup(s) water')
print(str('{:.2f}'.format(newagavenectar/16))+' cup(s) agave nectar')