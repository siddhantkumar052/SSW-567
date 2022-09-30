"""
Name: Siddhantkumar Maske
Cwid:20006862
Subject: SSW 567
HW HW 02b Continuous Integration - Classify Triangle
"""
import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(3, 4, 0), 'InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(-1, -4, 5), 'InvalidInput')

    def testInvalidInput3(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'InvalidInput')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(10, 2, 3), 'NotATriangle')

    def testNotATriangle5(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'NotATriangle')

    def testNotATriangle6(self):
        self.assertNotEqual(classifyTriangle(5, 5, 8), 'NotATriangle')

    def testRightTriangle7(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangle8(self):
        self.assertNotEqual(classifyTriangle(11, 11, 10), 'Right')

    def testEquilateralTriangle9(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def testEquilateralTriangles10(self):
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral')

    def testEquilateralTriangles11(self):
        self.assertNotEqual(classifyTriangle(4, 8, 10), 'Equilateral')

    def testIsoscelesTriangle12(self):
        self.assertEqual(classifyTriangle(4, 4, 5), 'Isosceles')

    def testIsoscelesTriangle13(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles')

    def testIsoscelesTriangle14(self):
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isosceles')

    def testScaleneTriangle15(self):
        self.assertEqual(classifyTriangle(4, 8, 10), 'Scalene')

    def testScaleneTriangle16(self):
        self.assertEqual(classifyTriangle(5, 9, 11), 'Scalene')

    def testScaleneTriangle17(self):
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
