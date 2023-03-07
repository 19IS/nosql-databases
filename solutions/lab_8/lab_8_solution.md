# Решение к лабораторной работе №8. Распределенные вычисления. `MapReduce` в `MongoDB`

## Задание 1. Создайте коллекцию документов для обработки её с помощью `MapReduce`.

- Запрос для создания новой коллекции `smartphones`:

    ```javascript
    use laptopsShop;
    db.createCollection("smartphones");
    ```

## Задание 2. Наполните коллекцию документами.

- Запрос для наполнения новой коллекции `smartphones` данными:

    ```javascript
    db.smartphones.insertMany([
        {name: "Nexus One", date: new Date(2013, 0, 20, 12, 00)},
        {name: "Nexus One", date: new Date(2013, 0, 20, 13, 00)},
        {name: "iPhone 4", date: new Date(2013, 0, 20, 13, 30)},
        {name: "Nexus One", date: new Date(2013, 0, 20, 14, 00)},
        {name: "iPhone 4", date: new Date(2013, 0, 21, 15, 30)},
        {name: "iPhone 4", date: new Date(2013, 0, 21, 15, 40)},
        {name: "Nexus One", date: new Date(2013, 0, 21, 16, 20)},
        {name: "iPhone 4", date: new Date(2013, 0, 21, 17, 00)},
        {name: "Nexus One", date: new Date(2013, 0, 21, 18, 00)},
        {name: "Nexus One", date: new Date(2013, 0, 22, 19, 00)}
    ]);
    ```

## Задание 3. Произведите обработку коллекции с использованием модели распределенных вычислений `MapReduce`.

- Запрос для создания функции `map`:
  ```javascript
  var map = function() {
      var key = {
          name: this.name,
          year: this.date.getFullYear(),
          month: this.date.getMonth(),
          day: this.date.getDate()
      };
      emit(key, {count: 1});
  };
  ```

- Запрос для создания функции `reduce`:

  ```javascript
  var reduce = function(key, values) {
      var sum = 0;
      values.forEach(function(value) {
          sum += value['count'];
      });
      return {count: sum};
  };
  ```
- Запрос для выполнения `mapReduce`

  ```javascript
  db.smartphones.mapReduce(map, reduce, {out: {inline: 1}});
  ```

  Результат запроса:
  ```javascript
  {
    results: [
      {
        _id: { name: 'iPhone 4', year: 2013, month: 0, day: 21 },
        value: { count: 3 }
      },
      {
        _id: { name: 'iPhone 4', year: 2013, month: 0, day: 20 },
        value: { count: 1 }
      },
      {
        _id: { name: 'Nexus One', year: 2013, month: 0, day: 21 },
        value: { count: 2 }
      },
      {
        _id: { name: 'Nexus One', year: 2013, month: 0, day: 22 },
        value: { count: 1 }
      },
      {
        _id: { name: 'Nexus One', year: 2013, month: 0, day: 20 },
        value: { count: 3 }
      }
    ],
    ok: 1
  }
  
  ```
  > **Note**: Однако `mapReduce` является устаревшим начиная с версии `MongoDB 5.0`
- Выполним запрос с использованием `aggregate`:

  ```javascript
  db.smartphones.aggregate([
      {
          $addFields: {
              "year": {
                  $year: "$date"
              },
              "month": {
                  $month: "$date"
              },
              "day": {
                  $dayOfMonth: "$date"
              },
              "count": 1
          }
      },
      {
          $group: {
              "_id": {
                  "name": "$name",
                  "year": "$year",
                  "month":  "$month",
                  "day": "$day"
              },
              "count": {$sum: "$count"}
          }
      },
      {
          $sort: {
              "name": -1
          }
      }
  ]);
  ```
> **Note**: Результат запроса немного отличается т.к. во-вопервых представленные выше функции (взятые из методичны) не корректно берут номер месяца (0-го месяца не бывает), а во-вторых результат агрегации выведен в виде поля, а не в виде значения поля `value`.
  ```javascript
  [
    {
      _id: { name: 'iPhone 4', year: 2013, month: 1, day: 21 },
      count: 3
    },
    {
      _id: { name: 'iPhone 4', year: 2013, month: 1, day: 20 },
      count: 1
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 1, day: 21 },
      count: 2
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 1, day: 22 },
      count: 1
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 1, day: 20 },
      count: 3
    }
  ]
  ```