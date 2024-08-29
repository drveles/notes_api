# API для заметок
*RESTfull* cервис для управления заметками <br>

Stack: `Python`, `MongoDB`, `Docker`, `FastAPI`, `aiohttp`, `asyncio`, `unittest` <br>

- Пользователи имеют доступ только к своим заметкам. <br>
- Заметки проверярются на орфографические ошибки используя API сервиса "Яндекс.Спеллер" <br>

## API - `FastAPI`
### Endpoints:
1. POST `http://host:port/add-note/`<br>
Добавление новой заметки пользователя в базу данных.<br>
2. GET `http://host:port/notes/`<br>
Возврат всех заметок пользователя в JSON формате.<br>

## Client - `aiohttp`
Сервис для взаимодействия с API и проведения интеграционных тестов.

## DB - `MongoDB` <br>
Считаю, что для текстовых заметок документоориентированная база данных подходходит идеально.<br>

``` json 
{
    "_id": auto
    "username": "str"
    "note": "str" 
    "have_typo": bool
}
```

## Tests


## TO DO 

- [x] Авторизация и аутентификация + тесты.
- [ ] API:
    - [x] Валидация через Спеллер
    - [x] Просмотр списка заметок
    - [x] Добавление заметки
    - [ ] Тесты
- [x] Починить общение контейнеров
- [ ] Терминальный интерфейс клиента и клиентские тесты.
- [x] Докеризация
- [x] База данных. Для MVP - просто json файлик, для релиза - MongoDB.
- [ ] Проверить все подсказки типов.
- [x] Проверить зависимости для АПИ, могут быть лишние.
- [ ] Документация, инструкция по тестированию.
