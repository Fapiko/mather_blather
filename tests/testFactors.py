import unittest
import factors

class TestFactors(unittest.TestCase):

	def testPrimeFactorization(self):
		self.assertListEqual([2, 3, 11, 19], factors.primeFactorization(1254))
		self.assertListEqual([431], factors.primeFactorization(431))
		self.assertListEqual([2, 2, 2, 11], factors.primeFactorization(88))

if __name__ == '__main__':
	unittest.main()
