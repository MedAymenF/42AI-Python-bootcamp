from book import Book
from recipe import Recipe
from datetime import datetime

om = Recipe('Omelette', 1, 5, ['Eggs', 'Cooking oil'], 'La ghla 3la mskin',
            'starter')
print(str(om))
recipe_book = Book('Paleo', datetime(2021, 1, 19), datetime(2021, 1, 17), {'starter': [om], 'lunch': 1, 'dessert': 2})
recipe_book.get_recipes_by_types('starter')
recipe_book.get_recipe_by_name('Omelette')