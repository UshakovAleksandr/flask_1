Процесс создания и запуска приложения в Docker
1. Создание образа - docker build --tag=flask-server .
2. Запуск контейнера - docker run -d --name my-flask-server -p 5000:5000 flask-server
    - проверка порта, на котором запустился gunicorn - docker container logs my-flask-server
3. Остановка контейнера - docker container stop my-flask-server
4. Удаление кнтейнера - docker container rm my-flask-server
