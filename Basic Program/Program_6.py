#take length and width from the user and find the area and perimeter of the rectangle

length = int(input("Enter the length:- "))
width = int(input("Enter the width:- "))
#perimeter=2l+2w
perimeter = (2*length) + (2*width)
print(f"the perimeter of rectangle is:- {perimeter} ")
#area=l*w
area = length * width
print(f"the area of rectangle is:- {area}")