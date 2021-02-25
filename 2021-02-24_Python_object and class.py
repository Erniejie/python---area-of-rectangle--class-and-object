#object and class in python- Computer Programming Tutor
# uploaded on Febr25,2021

# a very simple Class:

class Rectangle:
    # Attibute
    attr1 = 45
    attr2 = 68

    # Sample Method

    def Area_Rec(self):
        print("Length of a Rectangle:", self.attr1)
        print("Breath of a Rectangle:", self.attr2)
        print("The Area is :",  self.attr1+ self.attr2)

#Declaring an Object

My_Object = Rectangle()

# Accessing class attributes and method

print(My_Object.attr1,My_Object.attr2)
My_Object.Area_Rec()
