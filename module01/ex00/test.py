from book import Book
from recipe import Recipe
from datetime import datetime

om = Recipe('Omelette', 1, 5, ['Eggs', 'Cooking oil'], 'La ghla 3la mskin',
            'starter')
dinner = Recipe('Chicken', 4, 60, ['Chicken breast', 'Vegetables'],
                'La ghla 3la mskin', 'lunch')
recipe_book = Book('Paleo', datetime(2021, 1, 19), datetime(2021, 1, 17),
                   {'starter': [om], 'lunch': [], 'dessert': []})
recipe_book.get_recipes_by_types('starter')
recipe_book.get_recipe_by_name('Omelette')
recipe_book.add_recipe(dinner)
print(recipe_book.last_update)
ret = recipe_book.get_recipe_by_name('Chicken')
recipe_book.get_recipes_by_types('lunch')
