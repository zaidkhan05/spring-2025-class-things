import unittest
from party_hats import find_missing_hat

tests = (
    (
        [0, 1, 3, 4],
        4,
        {2},
    ),
    (
        [6, 2, 4, 5, 0, 1, 3],
        7,
        {7},
    ),
    (
        [6, 8, 3, 2],
        8,
        {0, 1, 4, 5, 7},
    ),
    (
        [],
        12,
        set(range(13)),
    ),
    (
        [3,2,5,4,6,1],
        6,
        {0}
    ),
    (
        [4,2,6,0,1,5],
        6,
        {3}
    ),
)

def check(test):
    A, N, staff_sol = test
    student_sol = find_missing_hat(A, N)
    return student_sol in staff_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))
    def test_06(self): self.assertTrue(check(tests[ 5]))

if __name__ == '__main__':
    res = unittest.main(verbosity = 3, exit = False)
