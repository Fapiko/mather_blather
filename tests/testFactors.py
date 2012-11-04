import unittest
import factors

class TestFactors(unittest.TestCase):

	def testPrimeFactorization(self):
		self.assertListEqual([2, 3, 11, 19], factors.primeFactorization(1254))
		self.assertListEqual([431], factors.primeFactorization(431))
		self.assertListEqual([2, 2, 2, 11], factors.primeFactorization(88))

	def testFactors(self):
		self.assertListEqual([1, 2, 5, 10], factors.factor(10))
		self.assertListEqual([1, 2, 5, 10, 25, 50], factors.factor(100))

	def testGreatestCommonDivisor(self):
		self.assertEqual(10, factors.greatestCommonDivisor(50, 10))
		self.assertEqual(5, factors.greatestCommonDivisor(5, 10))
		self.assertEqual(1, factors.greatestCommonFactor(21, 58))


if __name__ == '__main__':
	unittest.main()
