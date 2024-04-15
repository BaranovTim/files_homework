cook_book = {}
ingredient_dict = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        recipe_name = f.readline().strip()
        recipe_quantity = int(f.readline().strip())

        ingredients_list = []
        for i in range(recipe_quantity, 0, -1):
            ingredient_line = f.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split('|')
            ingredients_list.append({
                'ingredient_name': ingredient_name.strip(' '),
                'quantity': quantity.strip(' '),
                'measure': measure.strip(' \n')
            })

        cook_book[recipe_name] = ingredients_list

print(cook_book)
