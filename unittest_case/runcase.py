#coding=utf-8
# import sys
# sys.path.append('D:\Test')
# import unittest
# from unittest_case.test_case01 import TestCase01
# from unittest_case.test_case02 import TestCase02
# from unittest_case.test_case03 import TestCase03

# case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)

# suite = unittest.TestSuite([case_01,case_02,case_03])
# unittest.TextTestRunner().run(suite)
 
import sys
import os
import unittest
case_path = os.getcwd()+"\\unittest_case"
print(case_path)

discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)
