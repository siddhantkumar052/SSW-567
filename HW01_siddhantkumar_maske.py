#HW 01: Testing triangle classification
#Name: Siddhantkumar Maske  
#Cwid: 20006862

import unittest   

def is_valid_triangle(a,b,c):
    if (a+b)>=c and (b+c)>=a and (c+a)>=b:
        return 'True'
    else:
        return 'False'

def classify_triangle(a,b,c):
    if a == b and b == c:
        print("The triangle is an equilateral triangle")
        triangle_type = 'Equilateral'
    elif a==b or b==c:
        print("The triangle is an Isosceles triangle")
        triangle_type = 'Isosceles'
    else:
        print("The triangle is an Scalene triangle")
        triangle_type = 'Scalene'
    return triangle_type

def right_angle(a, b, c):
    if (a * a) + (b * b) == (c * c):
        triangle_type = 'Right'
    return triangle_type

def main():
    print("Input lengths of the triangle sides: ")
    a = int(input("Length of first side: "))
    b = int(input("Length of second side: "))
    c = int(input("Length of third side: "))

class TestTriangles(unittest.TestCase):
    def testSet1(self): self.assertEqual(is_valid_triangle(10,2,3),'False')
    def testSet2(self): self.assertEqual(is_valid_triangle(3, 4, 5),'True')
    def testSet3(self): self.assertEqual(classify_triangle(5,5,5),'Equilateral')
    def testSet4(self): self.assertNotEqual(classify_triangle(5,6,7),'Equilateral')
    def testSet5(self): self.assertEqual(classify_triangle(5,5,8),'Isosceles')
    def testSet6(self): self.assertNotEqual(classify_triangle(4,5,8),'Isosceles')
    def testSet7(self): self.assertEqual(classify_triangle(4,8,10),'Scalene')
    def testSet8(self): self.assertNotEqual(classify_triangle(11,11,10),'Scalene')
    def testSet9(self): self.assertEqual(right_angle(8,15,17),'Right')   
    def testSet10(self): self.assertNotEqual(right_angle(10,10,10),'Right')  
            
if __name__ == '__main__':
    is_valid_triangle
    classify_triangle
    right_angle
    unittest.main(exit=False,verbosity=2)
