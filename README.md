## Question 1
using if-elif, write a Python program that reports the contents of a compressed-gas cylinder based on the cylinder’s color. The color name i.e. orange or brown etc.. can be entered as lower case or upper case letters but make sure the spelling is correct. 
Cylinder colors and associated contents are as follows:

- orange ammonia
- brown carbon monoxide
- yellow hydrogen
- green oxygen

If the color is not one of the four names mentioned above, your program displays "Contents unknown".

## Question 2
We can form the 3 sides of a right angle triangle using the following formula:<br>
$side1=m^2-n^2$<br>
$side2=2mn$<br>
$hypotenuse=m^2+n^2$<br>
where m and n are two positives integers with m > n.

Write a Python program that reads 2 positive integers in any order.  Then, after validating the input, it will assign the largest value to m and the smallest to n and compute and display the three sides of the right angle triangle as shown in the sample runs.

**Note** that the Pythagorean theorem states that the sum of the squares of the sides of
a right triangle is equal to the square of the hypotenuse

## Question 3
Write a Python program that promts the user to enter the sides of a triangle. After checking each side which must be positive, it will display one the following messages:
- The input values cannot represent the sides of a triangle
- Equilateral triangle
- Isosceles triangle
- Scalene triangle 

The first check is that all sides must be positive. If one of the sides is not positive, the program will display error message and stops and does not continue reading the remaining sides.<br> 
The condition for the sides to form a triangle is that the sum of any 2 sides must be greater than the third side.<br>
For the remaining cases, the conditions are as follows:<br>
- Equilateral triangle, all sides are equal.
- Isosceles triangle, two of the 3 sides are equal.
- Scalene triangle, all three sides are different.

**Note** that your output message must match exactly the strings displayed by the sample runs. 
