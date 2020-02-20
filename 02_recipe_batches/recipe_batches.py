#!/usr/bin/python

import math
# https://www.programiz.com/python-programming/methods/dictionary/get


def recipe_batches(recipe, ingredients):
    ingredients_recipe_ratios = []
    for ingredient, value in recipe.items(): #o(n)
        ratio = ingredients.get(ingredient, 0) // value
        ingredients_recipe_ratios.append(ratio)
    ## can also do action for i, j in object
    smallest_amount_ingredient = min(ingredients_recipe_ratios) #o(n)
    maximum_batches = smallest_amount_ingredient
    return maximum_batches

# like stock prices track maximum batches
    #   if profit > largest_profit:
    #       largest_profit = profit

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
