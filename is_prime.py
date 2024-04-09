import unittest

def is_prime(value):
    if value < 2:
        return False
    for i in range (2, value):
         if value % i == 0:
            return False
    return True


class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertFalse(result)
    
    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)

    def test_with_6(self):
        result = is_prime(6)
        self.assertFalse(result)
    
    def test_with_7(self):
        result = is_prime(7)
        self.assertTrue(result)
    
    def test_with_8(self):
        result = is_prime(8)
        self.assertFalse(result)
    
    def test_with_9(self):
        result = is_prime(9)
        self.assertFalse(result)
    
    def test_with_10(self):
        result = is_prime(10)
        self.assertFalse(result)    
unittest.main()