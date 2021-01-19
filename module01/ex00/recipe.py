class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        if (type(name) is not str or not len(name)):
            print("Name must be a non-empty string")
            exit()
        self.name = name
        if (type(cooking_lvl) is not int
                or cooking_lvl < 1 or cooking_lvl > 5):
            print("Cooking level must be a number from 1 to 5")
            exit()
        self.cooking_lvl = cooking_lvl
        if (type(cooking_time) is not int or cooking_time < 0):
            print("Cooking time must be a positive number")
            exit()
        self.cooking_time = cooking_time
        if (type(ingredients) is not list):
            print("Ingredients must be a list")
            exit()
        for item in ingredients:
            if (type(item) is not str):
                print("Each ingredient must be a string")
                exit()
        self.ingredients = ingredients
        if (type(description) is not str):
            print("Description must be a string")
            exit()
        self.description = description
        if (type(recipe_type) is not str
                or recipe_type not in ["starter", "lunch", "dessert"]):
            print("Recipe type can only be “starter”, “lunch” or “dessert”")
            exit()
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Name: {self.name}\
\nCooking level: {self.cooking_lvl}\
\nCooking time: {self.cooking_time} minutes\
\nIngredients: {self.ingredients}\
\nRecipe type: {self.recipe_type}\
\nDescription: {self.description}"
        return txt
