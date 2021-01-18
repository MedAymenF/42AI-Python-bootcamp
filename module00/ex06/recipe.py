cookbook = {}


def print_recipe(recipe):
    if (recipe in cookbook):
        print('Recipe for {}:'.format(recipe))
        print('Ingredients list: {}'.format(cookbook[recipe]['ingredients']))
        print('To be eaten for {}.'.format(cookbook[recipe]['meal']))
        print('Takes {} of cooking.'.format(cookbook[recipe]['prep_time']))


def delete_recipe(recipe):
    if (recipe in cookbook):
        del(cookbook[recipe])


def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {'ingredients': ingredients,
                        'meal': meal, 'prep_time': prep_time}


def print_cookbook():
    for recipe in cookbook.keys():
        print(recipe)


def dispatcher(value):
    if (value == 1):
        recipe = input("\nPlease enter the name of the recipe to add:\n>> ")
        ingredients = input("\nPlease enter the\
 ingredients to add:\n>> ").split()
        meal = input("\nPlease enter the meal to add:\n>> ")
        prep_time = input("\nPlease enter the prep_time to add:\n>> ")
        add_recipe(recipe, ingredients, meal, prep_time)
    elif (value == 2):
        recipe = input("\nPlease enter the name of the recipe to delete:\n>> ")
        delete_recipe(recipe)
    elif (value == 3):
        recipe = input("\nPlease enter the recipe's name\
 to get its details:\n>> ")
        print_recipe(recipe)
        print('\n')
    elif (value == 4):
        print_cookbook()
    else:
        exit()


if __name__ == '__main__':
    add_recipe(
        'sandwich',
        ['ham', 'bread', 'cheese', 'tomatoes'],
        'lunch', '10 minutes')
    add_recipe('cake', ['flour', 'sugar', 'eggs'], 'dessert', '60 minutes')
    add_recipe(
        'salad',
        ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'lunch', '15 minutes')
    while (True):
        value = input('Please select an option by typing\
 the corresponding number:\
 \n1: Add a recipe\
 \n2: Delete a recipe\
 \n3: Print a recipe\
 \n4: Print the cookbook\
 \n5: Quit\n>> ')
        if (value.isnumeric() and 0 < int(value) < 6):
            dispatcher(int(value))
        else:
            while (True):
                value = input('This option does not exist\
, please type the corresponding number.\nTo exit, enter 5.\n\
>> ')
                if (value.isnumeric() and 0 < int(value) < 6):
                    break
            dispatcher(int(value))
