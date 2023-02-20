import random
import json

MANUFACTURERS = [
    'Apple',
    'Dell',
    'Lenovo',
    'HP',
    'Acer',
    'Asus',
    'MSI',
    'Samsung',
    'Razer',
    'Microsoft'
]

MODELS = [
    'Laptop Legend',
    'Speedo Ninja',
    'Laptop Lothario',
    'Pixelated Prince',
    'My Love and Life',
    'Keyboard Kombatant',
    'Binary Baron',
    'Laptop Leviathan',
    'Notebook Ninja',
    'Laptopinator',
    'Bombastic',
    'Laptop Lord',
    'Digital Duke',
    'Techno Tyrant',
    'Lord of Laptops',
    'Fast and Laptorious',
    'Laptop Laird',
    'Computing Crusader',
    'Notebook Noble',
    'Data Duke',
    '007 Buddy',
    'Cyber Count',
    'Digital Duchess',
    'Lappy Mc Lappface',
    'Laptop Luminary',
    'Laptopinator',
    'Hp Blaster',
    'Circuitry Countess',
    'Portable Pump',
    'Laptop Lady',
    'Wish Comes',
    'Silicon Squire'
]

COLORS = ['blue', 'carbon', 'yellow', 'red', 'grey', 'black', 'white']


def run():
    notebooks_collection = []
    for index in range(100):
        manufacturer = random.choice(MANUFACTURERS)
        model = random.choice(MODELS)
        notebooks_collection.append({})
        notebooks_collection[index]['code'] = None
        notebooks_collection[index]['name'] = f"{manufacturer} {model}"
        notebooks_collection[index]['img'] = None
        notebooks_collection[index]['specs'] = {
            'manufacturer': manufacturer,
            'model': model
        }
        notebooks_collection[index]['in_stock'] = random.choice([True, False])
        notebooks_collection[index]['colors'] = random.choices(COLORS, k=3)
        notebooks_collection[index]['price'] = round(random.uniform(6000.0, 30000.0), 1)

    with open('lab_4_laptops_docs.json', 'w') as file:
        json.dump(notebooks_collection, file, indent=4)


if __name__ == '__main__':
    run()
