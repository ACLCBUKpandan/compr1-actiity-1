import unittest
from exercise import exercise4
from test.utils import info,reset,success,err,warn
def test_nums(operation,temp,expected):
	B=expected;A=operation;C=exercise4.convert_temperature(A,temp);info(f"Testing the value: {A} | {temp}°C")
	if C==B:
		if not(A=='K'or A=='F'):warn('BONUS: ');warn(f"Expected: {B} | Result : {C} ")
		else:info(f"Expected: {B} | Result : {C} ")
		success('OK');return
	raise ValueError(f" Expected: {B} | Result : {C}")
class Test1(unittest.TestCase):
	def test_calculation(F):
		C='--------------';print('===== Exercise 4 ===== ');info('Testing set of numbers');B=('K',100,373.15),('F',1,33.8),('K',18,291.15),('F',18,64.4),('F',36,96.8),('ABC',123,'error')
		try:
			for(D,A)in enumerate(B):info(f"[{D+1} / {len(B)}]");info(C);test_nums(A[0],A[1],A[2]);info(C)
		except ValueError as E:err(f"{E}")
if __name__=='__main__':unittest.main()