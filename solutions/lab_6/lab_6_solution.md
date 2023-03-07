# Решение к Лабораторной работе №6. Запросы: модификаторы массивов. Позиционные модификаторы массивов

## Задание 1. Создайте несколько запросов для вставки данных в массив

- Запрос на добавление цвета "orange" для всех ноутбуков от "Apple"

    ```javascript
    db.laptops.updateMany({"specs.manufacturer": "Apple"}, { $push: {colors: 'orange'}});
    ```
  
- Запрос на добавление цвета "titan" для всех ноутбуков от 10000.0 руб. и выше

    ```javascript
    db.laptops.updateMany({"price": { $gte: 10000.0 }}, { $push: {colors: 'titan'}});
    ```
  

## Задание 2. Создайте запросы, производящие обновление данных в массиве: как по позиции элемента в массиве, так и по его значению

- Запрос на обновление значения "red" в массиве "colors" на "sky blue" для всех ноутбуков

    ```javascript
    db.laptops.updateMany({"colors": "red"}, { $set: {"colors.$": "sky blue"}});
    ```
  
- Запрос на обновление второго значения (index = 1) в массиве "colors" на "orange" для всех ноутбуков

    ```javascript
    db.laptops.updateMany({}, { $set: {"colors.1": "orange"}});
    ```

## Задание 3. Создайте запросы, удаляющие элементы из массива: по позиции элемента в массиве и по его значению.

- Запрос на удаление значения "sky blue" в массиве "colors" для всех ноутбуков

    ```javascript
    db.laptops.updateMany({}, { $pull: {"colors": "sky blue"}});
    ```
  
- Запрос на удаление первого значения (index = 1) в массиве "colors" для всех ноутбуков

    ```javascript
    db.laptops.updateMany({}, { $unset: {"colors.0": 1}});
    db.laptops.updateMany({}, { $pull: {"colors": null}});
    ```
