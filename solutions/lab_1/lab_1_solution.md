# Решение к Лабораторной работе №1. Установка и настройка `MongoDB`

> :warning: Пункты 1-3 описаны в самой лаборатоной работе. Поэтому решение сразу будет начинаться с пункта 4.

> :warning: Все пункты задания выполнены с помощью `MongoDB Shell`. Однако вы можете использовать графическую оболочку `MongoDB Compass`

## Задание 4. Создать БД с названием 19IS

```shell
use 19IS
```

## Задание 5. В 19IS создать коллекцию main_collection

```shell
db.createCollection("main_collection")
```

## Задание 6. В коллекции создать документ, в котором будет следующие поля: `first_name`, `last_name`

```shell
db.main_collection.insertOne({"_id": 1, "first_name": "Andrew", "last_name": "Chuiko"});
```
