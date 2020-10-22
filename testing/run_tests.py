import sys
import unittest


modules_to_test = [
    'Pieces',
    'Board',
    'Game'
    ]


def suite():
    tests = unittest.TestSuite()
    for module in map(__import__, modules_to_test):
        tests.addTest(unittest.findTestCases(module))
    return tests


if __name__ == '__main__':
    sys.path.append(r'./chess')
    unittest.TextTestRunner(verbosity=2).run(suite())
