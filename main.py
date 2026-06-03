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