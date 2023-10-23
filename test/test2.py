from colorama import Fore,Style,Back
import unittest
from exercise import exercise2
from test.utils import info,reset,success,err
def calculate_test(l,w):
	info(f"   > Testing length: {l}, width: {w}");A=exercise2.calculate_rectangle(l,w);info(f"    > Results: {A}")
	if A==l*w:success(f"    > OK")
	else:err(f"    > Expected Result: {l*w}");reset();raise ValueError('Wrong Results')
class Test1(unittest.TestCase):
	def test_calculation(E):
		print('===== Exercise 2 ===== ');info('Testing set of numbers')
		try:
			B=(2,2),(4,20),(6,9)
			for(C,A)in enumerate(B):print(A);info(f"[{C+1} / {len(A)+1}]");calculate_test(A[0],A[1])
		except ValueError as D:err(f"{D}")
if __name__=='__main__':unittest.main()