API сервис по загрузке изображений в базу данных с последующей обработкой с использованием библиотеки Pillow.

Сервис готов к работе, осталось только 
1. Клонировать репозиторий и зайти в него  
git clone https://github.com/Tisot-studio/image_api.git  
cd image_api

2. Создать виртуальное окружение и запустить его, например:  
py -m venv testenv  
testenv\Scripts\activate 

3. Установить все необходимые пакеты:  
pip install -r requirements.txt

4. Запустить сервер  
py manage.py runserver

Можно создавать запросы через Postman! :)

1. Получить список всех изображений метод - GET  
  http://localhost:8000/api/images/

2. Получить изображение по его id, метод GET  
  http://localhost:8000/api/images/1/

3. Загрузить изображение (файл/url) в БД, метод POST
  http://localhost:8000/api/images/
 
4. Изменить размеры конкретного изображения (указывается id). В форме указать KEY: width и height VALUE: 500 и 600 (например), метод POST  
  http://localhost:8000/api/images/1/resize/
  
5. Удалить изображение (указывается id), метод DELETE  
  http://localhost:8000/api/images/13/
