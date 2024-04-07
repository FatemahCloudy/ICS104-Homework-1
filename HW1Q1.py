# Your code for Question 1 in this cell
# After you finish writing your code and check that it is working correctly, 
# uncomment the first line (#%%writefile HW1Q1.py) and run your code again so that 
#it genrates HW1Q1.py file

##

#Ask about colour
colour = input("What is the colour of the cylender?")
colour = colour.lower()

#If statments
if colour == "orange":
    print("The contents is ammonia")
elif colour == "brown":
    print("The contents is carbon monoxide")
elif colour == "yellow":
    print("The contents is hydrogen")
elif colour == "green":
    print("The contents is oxygen")
else:
    print ("Contents unknown")

#end
