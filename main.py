class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, x):
        if x <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(x)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except (TypeError, ValueError):
            return False

    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError
        
        return Recipe(self.title, [Ingredient(i.name, i.quantity * ratio, i.unit) for i in self.ingredients])

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = f"{self.title}:\n"
        for ing in self.ingredients:
            result += f"  - {ing}\n"
        return result.rstrip()

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, n):
        if n <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        for i in recipe.scale(n).ingredients:
            self._items.append((i, recipe.title))

    def remove_recipe(self, title):
        self._items = [i for i in self._items if i[1] != title]
 
    def get_list(self):
        a = {}
        for i, _ in self._items:
            k = (i.name, i.unit)
            if k in a:
                a[k] += i.quantity
            else:
                a[k] = i.quantity
        
        return sorted([Ingredient(name, quantity, unit) for (name, unit), quantity in a.items()], key=lambda x: x.name)

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list