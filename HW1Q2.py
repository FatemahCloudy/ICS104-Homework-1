# Your code for Question 2 in this cell
# After you finish writing your code and check that it is working correctly, 
# uncomment the first line and run your code again so that it genrates HW1Q2.py file

##

#get two numbers from user and chek if they are positive and different

num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter a different positive integer: "))
if num1 == num2:
  print ("The numbers should be different than each other")
elif num1 > 0 and num2 > 0:
	#assign m, n values
	m = max(num1,num2)
	n = min(num1,num2)
	#caculations
	side1 = m**2 - n**2
	side2 = 2 * m * n
	hypotenuse = m**2 + n**2
	#output
	print("The sides of the triangle are:")
	print("Side1 =", side1)
	print("Side2 =", side2)
	print("Hypotenuse =", hypotenuse)
elif num1 <= 0:
	print ("The first number should be positive")
elif num2 <= 0:
	print ("The second number should be positive")
	


#end
