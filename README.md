Шаблон сервиса для взаимодействия между голосовым помощником и NLU фреймворком. На данный момент реализованный сервис может быть обеспечивать взаимодействие между навыком Маруси и DialogFlow.

Новый навык Маруси <-> heroku-flask-chatbot <-> DialogFlow

План запуска использования навыка Маруси через DialogFlow и heroku-flask-chatbot:
1. Создать агента DialogFlow ([Создание нового агента DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/build-agent))
2. Подключить агента к проекту Google Cloud ([Создание нового проекта Google Cloud](https://cloud.google.com/dialogflow/es/docs/quick/setup#project))
3. Получить API ключ к проекту Google Cloud и сохранить в директорию с heroku-flask-chatbot ([Создание служебного аккаунта и загрузка приватного ключа](https://cloud.google.com/dialogflow/es/docs/quick/setup#sa-create))
4. Создать проект (app) в heroku ([Создание приложения на heroku](https://devcenter.heroku.com/articles/getting-started-with-python))
5. Определить переменные окружения в новом проекте heroku ([Создание переменных окружения heroku](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard)):
    - DIALOGFLOW_LANGUAGE_CODE = ru
    - GOOGLE_PROJECT_ID = `<Название проекта Google Cloud см п.2>`
    - DIALOGFLOW_SESSION_ID = `<Любое название сессии>`
    - GOOGLE_APPLICATION_CREDENTIALS = `<Имя файла API ключа к проекту Google Cloud см п.3>`
6. Собрать докер образ heroku-flask-chatbot и развернуть его на heroku ([Разворачивание сервиса на heroku с помощью докера](https://devcenter.heroku.com/categories/deploying-with-docker))
7. Создать новый навык Маруси ([Создание нового навыка Маруси](https://vk.com/dev/marusia_skill_docs))
8. В поле "Webhook URL" введите адрес сервиса в heroku см п.4