import unittest
from k_map_minimisation import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		"""tests the function called minFunc"""
		self.assertEqual(minFunc(4,"(0,1,2,3,4,5,6,7,8,9,10,11,12,13) d (14,15)"),"1")
		self.assertEqual(minFunc(4,"() d (1,4,5)"),"0")
		self.assertIn(minFunc(4,"(0,3,5,6,12,15,9,10) d -"),"wxyz + wxy'z' + wx'yz' + wx'y'z + w'xyz' + w'xy'z + w'x'yz + w'x'y'z'")
		self.assertIn(minFunc(4,"(0,1,3,4,5,6,7,12,13,14,15,9,11) d -"),"w'y' + x + z")
		self.assertIn(minFunc(4,"(5,7) d (3,2,6,15,14,11,10)"),"w'xz")
		self.assertIn(minFunc(4,"(0,2,4,5,6,12,15,14,8,10) d (7)"),"w'x + xy + z'")
		self.assertIn(minFunc(4,"(0,2,5,7,13,15,8,10) d -"),"xz + x'z'")
		self.assertIn(minFunc(4,"(1,3,7,11,15) d (0,2,5)"),"w'x' + yz or w'z + yz")
		self.assertIn(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14) d -"),"w'z' + xz' + y'")
		self.assertIn(minFunc(4,"(0,1,3,4,5,6,13,14,15,8,11) d (2,12)"),"wyz + w'x' + xy' + xz' + y'z' or wx + w'y' + x'yz + xz' + y'z' or wx + w'y' + w'z' + x'yz + y'z'")
		self.assertIn(minFunc(3,"(1,3,4,5,6,7) d -"),"w + y")
		self.assertEqual(minFunc(3,"(0,1,3,5,6,7) d (2,4)"),"1")
		self.assertIn(minFunc(3,"(1,2,4,5,7) d (3,6)"),"w + x + y")
		self.assertIn(minFunc(3,"(0,1,2,5) d -"),"w'y' + x'y")
		self.assertIn(minFunc(2,"(0,1,2) d -"),"w' + x'")
		
                
if __name__=='__main__':
	unittest.main()
