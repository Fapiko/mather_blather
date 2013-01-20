import unittest
from mather_blather import parser

class TestParser(unittest.TestCase):

	def testDistribute(self):
		self.assertEqual('2x+6.0+64.0y+2z+2a+2b+2c+5+3y-6.0', parser.distribute('2(x+3+32y+z+a+b+c)+5+3(y-2)'))


if __name__ == '__main__':
	unittest.main()