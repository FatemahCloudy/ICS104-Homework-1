# take three values from the user separated by ","
num = input("Enter three positive values speraterd by ',': ")

# split and convert each values to floats
values = [float(x) for x in num.split(",")]

# sort the values starting from the largest one
values.sort(reverse=True)

# assign avlues to a, b, and c
a, b, c = values

# now check if they are all positive numbers

if a > 0 and b > 0 and c > 0:
    # if they are all positive, determain the type of traingle
    if (b+c) < a:
        print("The values cannot represent tringle's sides ")
    elif a == b == c:
        print("The traingle is Equilateral")
    elif a == b:
        print("The traingle is Isosceles")
    elif b == c:
        print("The traingle is Isosceles")
    elif b!=c!=a:
        print("The traingle is Scalene")
#otherwise, display an error sentence
elif a <= 0:
    print("The values should be positive and nonzero")
elif b <= 0:
    print("The values should be positive and nonzero")
elif c <= 0:
    print("The values should be positive and nonzero")


#end
