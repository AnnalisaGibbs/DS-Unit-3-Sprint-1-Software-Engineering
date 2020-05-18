#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, .5)

    def test_default_product_stealability(self):
        """Test default product stealability isn't so stealable."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_default_product_explodability(self):
        """Test default product explodability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        """Test default number of products generated being 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test names are in ADJECTIVES and NOUNS."""
        products = generate_products()

        for product in products:
            names = product.name.split(" ")
            self.assertIn(names[0], ADJECTIVES)
            self.assertIn(names[1], NOUNS)

if __name__ == '__main__':
    unittest.main()