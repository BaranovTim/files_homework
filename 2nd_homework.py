with open('recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cook_name = line.strip()
        ingredients_qty = int(f.readline())
        ingredients = []

print(cook_name)
