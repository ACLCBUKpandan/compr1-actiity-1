import unittest
from exercise import exercise3
from test.utils import info,reset,success,err
def test_nums(num,expected):
	A=expected;B=exercise3.even_or_odd(num);info(f"Testing the value {num}")
	if B==A:info(f"Expected: {A} | Result : {B} ");success('OK');return
	raise ValueError(f" Expected: {A} | Result : {B}")
class Test1(unittest.TestCase):
	def test_calculation(H):
		D='--------------';C='odd';B='even';print('===== Exercise 3 ===== ');info('Testing set of numbers');E=(2,B),(10,B),(95,C),(-45,C),(-100001,C),(6,B)
		try:
			for(F,A)in enumerate(E):info(f"[{F+1} / {len(E)+1}]");info(D);test_nums(A[0],A[1]);info(D)
		except ValueError as G:err(f"{G}")
if __name__=='__main__':unittest.main()