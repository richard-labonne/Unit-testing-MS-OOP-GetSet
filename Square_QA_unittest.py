import unittest
import Square

#QA
        
class test_Square(unittest.TestCase):
    #square with positive sides - box with an area should be created
    def test_pos_creation(self):
        for side in range(1,101):
            h = w = side
            my_box = Square.Square(h,w)
            actual = my_box.height * my_box.width
            expected= side * side
            self.assertEqual(actual, expected)
           
 
    #square with negative sides - should give Exception("Value must be larger than 0") 
    def test_neg_creation(self):
        for side in range(-1, -101):
            h = w = side
            with self.assertRaises(Exception) as quarantine:
                Square.Square(h,w)                                   # https://docs.python.org/3/library/unittest.html#basic-example
            actual = str(quarantine.exception)       
            expected = "Value must be larger than 0"
            self.assertEqual(actual, expected)
            
     
    #square with 0 sides - should give Exception("Value must be larger than 0") 
    def test_0_creation(self):
        h = w = 0
        with self.assertRaises(Exception) as quarantine:
            Square.Square(h,w)
        actual = str(quarantine.exception)       
        expected = "Value must be larger than 0"
        self.assertEqual(actual, expected)

    #rectangle 1 - height constant should give Exception("Not Square")
    def test_rect_h(self):
        h = 1
        for w in range (2,101):
            with self.assertRaises(Exception) as quarantine:
                Square.Square(h,w)
        actual = str(quarantine.exception)       
        expected = "Not square"
        self.assertEqual(actual, expected)
        
    #rectangle 2 - width constant should give Exception("Not Square")
    def test_rect_w(self):
        w = 1
        for h in range (2,101):
            with self.assertRaises(Exception) as quarantine:
                Square.Square(h,w)
        actual = str(quarantine.exception)       
        expected = "Not square"
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()