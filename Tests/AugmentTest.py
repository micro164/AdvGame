import unittest

import sys
sys.path.insert(1, '../')

from Classes.Classes import Player
from Augment.Augment import augment


class AugmentTests(unittest.TestCase):
	def test_augment(self):
		result = augment(20, 10, 1, "weapon", "defense")
		self.assertEqual(result, 21)


if __name__ == '__main__':
	unittest.main()
