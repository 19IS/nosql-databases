# Лабораторная работа №1. Установка и настройка `MongoDB`

Для установки MongoDB необходимо установить следующие компоненты:

- `MongoDB`
- `MongoDB Shell` (оболочка для работы с базой данных)
- `MongoDB Compass` (графическая оболочка для работы с базой данных)

## Установка `MongoDB` и `MongoDB Compass`

> В лабораторных работах используется `MongoDB` версии `6.0.4`

Для установки MongoDB и MongoDB Compass необходимо скачать файл утановки с официального сайта MongoDB: https://www.mongodb.com/try/download/community.

Далее необходимо запустить скачанный файл установки `mongodb-windows-x86_64-6.0.4-signed`.

В открытом окне нажимаем `Next`

![img.png](../images/lab_1/img.png)

Устанавливаем галочку для пункта `I accept the terms in the License Agreement` и нажимаем `Next`

![img_1.png](../images/lab_1/img_1.png)

Выбираем тип установки `Complete`

![img_2.png](../images/lab_1/img_2.png)

Убираем галочку для пункта `Install MongoDB as a Servise` и нажимаем `Next`

![img_3.png](../images/lab_1/img_3.png)

Далее нам будет предложено установить `MongoDB Compass`. Устанавливаем галочку для пункта `Install MongoDB Compass` и нажимаем next

![img_4.png](../images/lab_1/img_4.png)

Подтверждаем установку, нажав на кнопку `Install`

![img_5.png](../images/lab_1/img_5.png)

После процесса установки нам будет выведенно соответствующее оповещение.

![img_6.png](../images/lab_1/img_6.png)

## Установка `MongoDB Shell`

`MongoDB Shell` не входит в стандартный пакет установки `MongoDB` и поэтому его нужно установить отдельно.

Для этого необходимо скачать архив с того же официального сайта: https://www.mongodb.com/try/download/shell .

Из данного архива нам необходим только файл `mongosh.exe`. Рекомендую его скопировать в ту же директорию, где находится и сам `MongoDB`: `C:\Program Files\MongoDB\Server\6.0\bin\`

## Настройка `MongoDB`

БД `MongoDB` неоходимо создать папку, в которой будут храниться данные. Для этого необходимо выполнить следующие шаги:

1. Создать директорию `mongo_db\data`:

```shell
 mkdir "C:\data\db"
```

2. Далее переходим в директорию, где установлено приложение `mongod`:

```shell
cd "C:\Program Files\MongoDB\Server\6.0\bin"
```

3. Вызываем команду для указания приложению папки для хранения данных:

> :warning: При первом запуске приложения `mongod.exe` может появиться предупреждение об опасности данного файла, т.к. по умолчанию в системе Windos запрещен запуск сценариев (скриптов).

```shell
./mongod.exe --dbpath="C:\data\db"
```

## Запуск сервера MongoDB

Для запуска сервера MongoDB необходимо запустить приложение mongod:

```shell
./mongod.exe
```

После чего будут выведены логи БД

![img_7.png](../images/lab_1/img_7.png)

## Подключение к серверу MongoDB с попощью `MongoDB Shell`:

> :warning: Перед подключением не забудте запустить сервер MongoDB.

Для подключения к серверу запустите mongosh, находящиеся в `C:\Program Files\MongoDB\Server\6.0\bin\`.

```shell
./mongosh
```

> При первом запуске mongosh программа может запросить строку подключения к БД. Необходимо просто нажать Enter.

После запуска mongosh и подключения к БД мы получаем доступ к выполнению различных команд, с помощью терминала.

![img_8.png](../images/lab_1/img_8.png)

## Подключение к серверу MongoDB с попощью `MongoDB Compass`:

Для подключения к серверу запустите приложение  `MongoDB Compass`.

![img_9.png](../images/lab_1/img_9.png)

Используем строку подключения по умолчанию (`mongodb://localhost:27017`) и нажимем `Connect`.

После чего мы получаем доступ к бд и должны видеть 3 базы по уполчанию:

- `admin`
- `config`
- `local`

![img_10.png](../images/lab_1/img_10.png)

## Задание на лабораторную работу

1. Установить MongoDB
2. Установить графическую оболочку `MongoDB Compas` и `MongoDB Shell`
3. Запустить сервер `MongoDB`
4. Создать БД с названием `19IS`
5. В `19IS` создать коллекцию main_collection
6. В коллекции создать документ, в котором будет следующие поля: `first_name`, `last_name`.

---

[Решение к лабораторной работе №1.](../solutions/lab_1/lab_1_solution.md)
