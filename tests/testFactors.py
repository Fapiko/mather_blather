import unittest
from mather_blather import factors

class TestFactors(unittest.TestCase):

	def testPrimeFactorization(self):
		self.assertListEqual([2, 3, 11, 19], factors.primeFactorization(1254))
		self.assertListEqual([431], factors.primeFactorization(431))
		self.assertListEqual([2, 2, 2, 11], factors.primeFactorization(88))

	def testFactors(self):
		self.assertEqual(set([1, 2, 5, 10]), factors.factor(10))
		self.assertEqual(set([1, 2, 100, 5, 10, 50, 20, 25, 4]), factors.factor(100))

	def testGreatestCommonDivisor(self):
		self.assertEqual(10, factors.greatestCommonDivisor(50, 10))
		self.assertEqual(5, factors.greatestCommonDivisor(5, 10))
		self.assertEqual(1, factors.greatestCommonFactor(21, 58))

	def testFindCommonDivisibilities(self):
		self.assertListEqual([2, 3, 4, 6, 8, 11, 12, 22, 24, 33, 44, 66, 88, 132, 264], factors.findCommonDivisibilities(22, 12, 15))

	def testLeastCommonMultiple(self):
		self.assertEqual(180, factors.leastCommonMultiple(18, 20))


if __name__ == '__main__':
	unittest.main()
