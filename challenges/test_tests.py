
import unittest   # The test framework
from basic_arithmetic_operations_on_a_string_number_hard import math
from Drunken_Python_medium import int_to_str, str_to_int
from Find_the_Discount_easy import dis
from Finding_Adjacent_Nodes_Meduim import adjacent
from How_Edabit_Works_Very_Easy import hello
from Imaginary_Coding_Interview_Hard import interview
from Return_the_Sum_of_Two_Numbers_Very_easy import sum
from Stuttering_Function_easy import stutter

class Test_basic_arithmetic_operations_on_a_string_number_hard(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(math("3 + 2"),5)
        self.assertEqual(math("3 - 2"),1)
        self.assertEqual(math("3 * 2"),6)
        self.assertEqual(math("3 // 0"),-1)
        self.assertEqual(math("8 // 2 "),4)

class Test_Drunken_Python_medium(unittest.TestCase):
    def test_int_to_str(self):
        self.assertEqual(int_to_str(5),"5")
    
    def test_str_to_int(self):    
        self.assertEqual(str_to_int("5"),5)

class Test_Find_the_Discount_easy(unittest.TestCase):
    def test_discountMethod(self):
        self.assertEqual(dis(100,75),25)

class Test_Finding_Adjacent_Nodes_Meduim(unittest.TestCase):
    def test_singleMethod(self):
        matrix = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
        self.assertEqual(adjacent(matrix,0,1),True)
        self.assertEqual(adjacent(matrix,2,0),False)

class Test_How_Edabit_Works_Very_Easy(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(),"hello edabit.com")

class Test_Imaginary_Coding_Interview_Hard(unittest.TestCase):
    def test_interview(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 120),"qualified")
        self.assertEqual(interview([5, 5, 10, 10, 25, 15, 20, 20], 120), "disqualified")

class Test_Return_the_Sum_of_Two_Numbers_Very_easy(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,7),9)

class Test_Stuttering_Function_easy(unittest.TestCase):
    def test_stutter(self):
        self.assertEqual(stutter("Hello"),"He... He... Hello?")

#class Test_







        


    

