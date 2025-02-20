import unittest
from find_first_missing_element import find_first_missing_element

tests = (
    (
        [1, 3, 4],
        1,
        2,
    ),
    (
        [1, 2, 3, 4, 5, 6], 
        1,
        7,
    ),
    (
        [3],
        3,
        4
    ),
    (
        [2, 3, 4, 5],
        1,
        1,
    ),
    (
        [2, 3, 4, 6, 7],
        5,
        5,
    ),
)

def check(test):
    arr, d, staff_sol = test
    student_sol = find_first_missing_element(arr, d)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
