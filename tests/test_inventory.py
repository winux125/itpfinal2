import unittest
import os
from services.inventory_mgr import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        # Use a temporary file for testing
        self.test_file = "test_data.json"
        # Create an empty file to start fresh
        with open(self.test_file, 'w') as f:
            f.write("[]")
        self.mgr = InventoryManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_product(self):
        result = self.mgr.add_product(1, "Test Laptop", 999.99, 10)
        self.assertTrue(result)
        self.assertEqual(len(self.mgr.get_all_products()), 1)
        
        # Test duplicate ID
        result_dup = self.mgr.add_product(1, "Another Laptop", 500.0, 5)
        self.assertFalse(result_dup)

    def test_remove_product(self):
        self.mgr.add_product(1, "Test Laptop", 999.99, 10)
        result = self.mgr.remove_product(1)
        self.assertTrue(result)
        self.assertEqual(len(self.mgr.get_all_products()), 0)

        # Test remove non-existent
        result_fake = self.mgr.remove_product(99)
        self.assertFalse(result_fake)

    def test_update_stock(self):
        self.mgr.add_product(1, "Test Laptop", 999.99, 10)
        
        # Add stock
        success, _ = self.mgr.update_stock(1, 5)
        self.assertTrue(success)
        self.assertEqual(self.mgr.inventory[1].quantity, 15)
        
        # Subtract stock
        success, _ = self.mgr.update_stock(1, -10)
        self.assertTrue(success)
        self.assertEqual(self.mgr.inventory[1].quantity, 5)
        
        # Prevent negative stock
        success, _ = self.mgr.update_stock(1, -10)
        self.assertFalse(success)
        self.assertEqual(self.mgr.inventory[1].quantity, 5) # unchanged

if __name__ == "__main__":
    unittest.main()
