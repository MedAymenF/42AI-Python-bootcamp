from datetime import datetime


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if (type(name) is not str):
            print("Name must be a string")
            exit()
        self.name = name
        if (type(last_update) is not datetime):
            print("Last update must be a datetime object")
            exit()
        self.last_update = last_update
        if (type(creation_date) is not datetime):
            print("Creation date must be a datetime object")
            exit()
        self.creation_date = creation_date
        if (type(recipes_list) is not dict or set(recipes_list.keys()) != set(["starter", "lunch", "dessert"])):
            print("Recipes list must be a dictionnary with 3 keys: “starter”, “lunch”, “dessert”")
            exit()
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipe in self.recipes_list.values():
            if (recipe.name == name):
                print(str(recipe))
                return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type not in ["starter", "lunch", "dessert"]):
            print("Recipe type can only be “starter”, “lunch” or “dessert”")
        else:
            for recipe in self.recipes_list[recipe_type]:
                print(recipe.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
