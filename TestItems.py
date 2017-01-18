import unittest
from Items import Item
from Enemy import *

class TestItems(unittest.TestCase):

    def test_item_was_created(self):

      flower = Item("Drew", "Guy with beard" , 1000)
      
      self.assertIsInstance(flower, Item)

    def test_is_enemy(self):
    	drew = Enemy("Drew" , 19 , 30)

     	self.assertIsInstance(drew, Enemy)



if __name__ == '__main__':
	unittest.main()








