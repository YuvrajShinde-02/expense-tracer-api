from django.test import TestCase
from restapi import models

# Create your tests here
class TestModel(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            descreption="anc headphones",
            category="music",
        )
        insertes_expense = models.Expense.objects.get(pk=expense.id)
        self.assertEqual(249.99, insertes_expense.amount)
        self.assertEqual("amazon", insertes_expense.merchant)
        self.assertEqual("anc headphones", insertes_expense.descreption)
        self.assertEqual("music", insertes_expense.category)
