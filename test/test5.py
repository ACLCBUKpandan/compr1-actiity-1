import unittest
from exercise import exercise5
from test.utils import info,reset,success,err,warn
def test_nums(operation,first_num,second_num,expected):
	E=second_num;D=first_num;C=operation;A=expected;B=exercise5.calculator(C,D,E);info(f"Testing the value: {D}  {C} {E} ")
	if B==A:
		if not C in['+','-','*','/']:warn('BONUS: ');warn(f"Expected: {A} | Result : {B} ")
		else:info(f"Expected: {A} | Result : {B} ")
		success('OK');return
	raise ValueError(f" Expected: {A} | Result : {B}")
class Test1(unittest.TestCase):
	def test_calculation(F):
		C='--------------';print('===== Exercise 5 ===== ');info('Testing set of numbers');B=('+',1,1,2),('-',1000,1,999),('*',5,5,25),('/',5,2,2.5),('+',10,15,25),('*',1024,50,51200),('Hello',123,134,'error')
		try:
			for(D,A)in enumerate(B):info(f"[{D+1} / {len(B)}]");info(C);test_nums(A[0],A[1],A[2],A[3]);info(C)
		except ValueError as E:err(f"{E}")
if __name__=='__main__':unittest.main()