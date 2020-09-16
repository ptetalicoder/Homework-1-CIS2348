# Pranav Tetali
# ID# 1541822

# Pranav Tetali
# ID#1541822

#1
def getCost(s):
    if s=="Oil change":
        return 35
    if s=="Tire rotation":
        return 19
    if s=="Car Wash":
        return 7
    if s=="Car wax":
        return 12
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

#2
print("Select first service:")
choice1=input()
print("Select second service:\n")
choice2=input()

#3
print("Davy's auto shop invoice")
print()
total=0

if choice1 == 'Oil change':
    print("Service 1: Oil change, $35")
    total = total + 35
elif choice1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total = total + 19
elif choice1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total = total + 7
elif choice1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total = total + 12
elif choice1 == '-':
    print('Service 1: No service')
    total = total + 0
else:
    print('Service 1: Invalid option')
if choice1 == 'Oil change':
    print('Service 2: Oil change, $35')
    total = total + 35
elif choice2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total = total + 19
elif choice2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total = total + 7
elif choice2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total = total + 12
elif choice2 == '-':
    print('Service 2: No service')
    total = total + 0
else:
    print('Service 2: Invalid option')
print()
print('Total: ${}'.format(total))