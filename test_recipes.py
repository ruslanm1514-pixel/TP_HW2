import pytest
from main import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient():
    test_1 = Ingredient("Мука", 500, "г")
    assert test_1.name == "Мука"
    assert test_1.quantity == 500
    assert test_1.unit == "г"
    assert Ingredient("Мука", 1000, "г") == test_1
    assert test_1 != Ingredient("Соль", 500, "г")
    assert test_1 != Ingredient("Мука", 500, "кг")

def test_recipe():
    test_ing = Ingredient("Мука", 200, "г")
    test_ing_2 = Ingredient("Мука", 300, "г")
    recipe = Recipe("Маргарита", [test_ing])
    assert recipe.title == "Маргарита"
    assert recipe.ingredients == [test_ing]
    recipe.add_ingredient(test_ing_2)
    recipe.add_ingredient(Ingredient("Соль", 500, "г"))
    assert recipe.ingredients[0].quantity == 500
    scaled = recipe.scale(10)
    assert scaled.ingredients[0].quantity == 5000
    assert recipe.ingredients[1].quantity == 500
    with pytest.raises(ValueError):
        recipe.scale(0)
    assert len(recipe) == 2

def test_shopping_list():
    test_1 = Recipe("1", [Ingredient("Мука", 500, "г"), Ingredient("Соль", 500, "г")])
    test_2 = Recipe("2", [Ingredient("Мука", 100, "г")])
    sl = ShoppingList()
    sl.add_recipe(test_1, 3)
    assert sl.get_list()[0].quantity == 1500
    with pytest.raises(ValueError):
        sl.add_recipe(test_1, 0)
    sl.add_recipe(test_2, 2)
    assert next(i for i in sl.get_list() if i.name == "Мука").quantity == 1700
    sl.remove_recipe("2")
    assert len(sl.get_list()) == 2
    assert sl.get_list()[0].quantity == 1500
