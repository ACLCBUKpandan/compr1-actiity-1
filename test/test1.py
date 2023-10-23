from colorama import Fore,Style,Back
import unittest
from exercise import exercise1
from test.utils import info,err,success
class Test1(unittest.TestCase):
	def test_name(A):
		print('===== Exercise 1 ===== ')
		try:info('[1 / 2] Checking if `name` variable exists...');exercise1.name
		except:err('Cannot find `name` variable.');return
		info('[2 / 2] Checking the value of `name`.')
		if exercise1.name=='James Paul':success('Testing Complete!')
		else:err('Wrong value of `name`.')
		print(Style.RESET_ALL)
if __name__=='__main__':unittest.main()