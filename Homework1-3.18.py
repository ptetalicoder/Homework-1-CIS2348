# Pranav Tetali
#Id 1541822

#1
import math
height=int(input("Enter wall height (feet):"))
width=int(input("Enter wall width (feet):"))
wall_area=(int(input("Wall area:\n")))
#2
wall_area = height*width
paint_needed = wall_area/350
cans=math.ceil(paint_needed)
#3
paint_colors_cost={"red":35,"blue":25,"green":23}
print("Wall area: " + str(wall_area) + " square feet")
print("Paint needed: {:.2f} gallons\n".format(paint_needed))
print("Cans needed: " + str(cans) + " can(s)\n")
color=input("Choose a color to paint the wall:\n")
cost=cans * paint_colors_cost[color.lower()]
print ("Cost of purchasing " + str(color) + " paint: $\n" + str(cost))