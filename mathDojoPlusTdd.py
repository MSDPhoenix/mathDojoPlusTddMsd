
import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self,num,*nums):
        self.result = self.result + num
        for i in nums:
            self.result += i
        return self
    def subtract(self,num,*nums):
        self.result = self.result - num
        for i in nums:
            self.result -= i
        return self

class MathDojoTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(self.x.add(1).result,1)
    def testCase2(self):
        self.assertEqual(self.x.subtract(1).result,-1)
    def testCase3(self):
        self.assertEqual(self.x.add(1,2).result,3)
    def testCase4(self):
        self.assertEqual(self.x.subtract(1,2).result,-3)
    def testCase5(self):
        self.assertEqual(self.x.add(1,2,3).result,6)
    def testCase6(self):
        self.assertEqual(self.x.subtract(1,2,3).result,-6)
    def setUp(self):
        print("setUp is running.")
        self.x = MathDojo()
    def tearDown(self):
        print("tearDown is running.")
        del self.x

if __name__ == "__main__":
    unittest.main()
