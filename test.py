"""
add(10,20)-->30
add(10,-20)-->-10
add("str1","str2")-->str1str2
add("str1",20)--> None
add(None,None)--> None
"""
from main import add 
import unittest

# res=add(10,20)
# if res!=30:
# 	raise Exception("test failed")

class TestAdd(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("login")
		cls.user="JAY"

	@classmethod
	def tearDownClass(cls):
		print("logout")
		cls.user=None


	def processing(self):
		print("this is proces")

	def setUp(self):
		print("CREATE resouces for test case")

	def tearDown(self):
		print("RELEASE the resource")

	def test1_add_10_20(self):
		print("execeting test1")
		print(self.user)
		act=add(10,20)
		exp=30
		error = "test_add_10_20 failed"
		self.assertEqual(act,exp,error)

	def test2_add_10_minus_20(self):
		print("execeting test2")
		print(self.user)
		act=add(10,-20)
		exp=-10
		error = "test_add_10_minus_20 failed"
		self.assertEqual(act,exp,error)

	def test3_str1_str2(self):
		print("execeting test3")
		print(self.user)
		act=add("str1","str2")
		exp="str1str2"
		error = "test3_str1_str2 failed"
		self.assertTrue(act==exp,error)

	def test4_str1_20(self):
		print("execeting test4")
		print(self.user)
		act=add("str1",20)
		exp=None
		error = "test4_str1_20 failed"
		self.assertTrue(act==exp,error)

if __name__ == "__main__":
	unittest.main()