import unittest
from order_management import Order

class TestOrderManagement(unittest.TestCase):

    def setUp(self):
        """Set up a fresh order before each test."""
        self.initial_items = [("Book", 2, 15.00), ("Pen", 5, 1.50)]
        self.order = Order("Alice", self.initial_items)

    # --- Unit Tests ---
    def test_calculate_total(self):
        """Unit Test: Verify total calculation logic."""
        # Book: 2 * 15 = 30. Pen: 5 * 1.5 = 7.5. Total = 37.5
        expected_total = 37.5
        self.assertEqual(self.order.calculate_total(), expected_total)

    def test_add_item(self):
        """Unit Test: Verify item addition."""
        self.order.add_item("Notebook", 1, 5.00)
        self.assertEqual(len(self.order.items), 3)
        self.assertEqual(self.order.items[-1][0], "Notebook")

    # --- Integration Test ---
    def test_order_lifecycle(self):
        """Integration Test: Create -> Add -> Remove -> Verify Total"""
        # 1. Start with Alice's order (Total 37.5)
        
        # 2. Add a Laptop (1 * 1000)
        self.order.add_item("Laptop", 1, 1000.00)
        
        # 3. Remove the Pens
        self.order.remove_item("Pen")
        
        # 4. Final Calculation should be:
        # Books (30) + Laptop (1000) = 1030.0
        self.assertEqual(self.order.calculate_total(), 1030.0)

if __name__ == '__main__':
    unittest.main()