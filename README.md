# Тестовое задание на позицию backend-разработчика от Avito Tech

## [Описание задания](https://t.me/pythontalk_ru/1511)

### Задача
* Создать сервис для хранения и подачи объявлений, объявления должны храниться в базе данных, а сам сервис должен предоставлять API, работающее поверх HTTP в формате JSON. Реализовать три метода: получение списка объявлений, получение одного объявления, создание объявления

### Информация по проекту
* Команда для запуска docker-compose up
* Покрытие тестами - 98%


### Метод получения списка объявлений:
* Роут для отправления GET запроса: http://localhost:8000/api/v1/advertisements/
* Реализована пагинация по 10 объявлений на странице;
* Реализована возможность сортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание). Параметры ?ordering=created_at / ?ordering=-created_at и
?ordering=price / ?ordering=-price
* В ответе выдаются следующие поля: название объявления, ссылка на главное фото (первое в списке), цена.

### Метод получения конкретного объявления:
* Роут для отправления GET запроса: http://localhost:8000/api/v1/advertisements/{id}/
* В ответе выдаются следующие поля(обязательные): название объявления, цена, ссылка на главное фото;
* При передаче дополнительного параметра ?fields=True добавятся следующие поля: описание, ссылки на все фото.

### Метод создания объявления:
* Роут для отправления POST запроса: http://localhost:8000/api/v1/advertisements/. В теле запроса необходимо передать 'name', 'price', 'description', 'uploaded_pictures'
* Запрос ️возвращает ID созданного объявления и код результата (ошибка или успех).
* Реализована валидация количества отправляемых изображений - не более 3х.
* Реализована валидация количества символов в описании - не больше 1000 символов
* Реализована валидация количества символов в названии - не больше 200 символов

