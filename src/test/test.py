import unittest

class BaseTest(unittest.TestCase):
    """Test Class"""

    def test_initial(self):
        self.assertAlmostEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
