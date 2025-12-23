import unittest
from timeout_decorator import timeout
from src.rotate_py.Solution_py import pySolution
from src.rotate_cpp.Solution_cpp import cppSolution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
            ([-1,-100,3,99], 2, [3,99,-1,-100]),
            ([1,5,3,2,7], 10000, [1,5,3,2,7]),
            ([1,2,3,4], 0, [1,2,3,4])
        )
        self.__solution_py = cppSolution()
        return super().setUp()
    
    @timeout(0.5)
    def testCase_0(self):
        nums, k, expectedOutput = self.__testcases[0]
        self.__solution_py.rotate(nums = nums, k = k)
        self.assertTrue(all(a == b for a, b in zip(nums, expectedOutput)))

    @timeout(0.5)
    def testCase_1(self):
        nums, k, expectedOutput = self.__testcases[1]
        self.__solution_py.rotate(nums = nums, k = k)
        self.assertTrue(all(a == b for a, b in zip(nums, expectedOutput)))

    @timeout(0.5)
    def testCase_2(self):
        nums, k, expectedOutput = self.__testcases[2]
        self.__solution_py.rotate(nums = nums, k = k)
        self.assertTrue(all(a == b for a, b in zip(nums, expectedOutput)))
    
    @timeout(0.5)
    def testCase_3(self):
        nums, k, expectedOutput = self.__testcases[3]
        self.__solution_py.rotate(nums = nums, k = k)
        self.assertTrue(all(a == b for a, b in zip(nums, expectedOutput)))

if __name__ == '__main__': unittest.main()