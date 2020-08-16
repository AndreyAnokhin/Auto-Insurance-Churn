## Описание тестового задания (свой реализованный проект) для Школы будущих СТО

### Название проекта

Прогнозирование оттока клиентов

### Какую задачу решает ваш проект?

Проект создан для демонстрации примера внедрении модели машинного обучения в продакшен. 
Суть модели - по данным клиента предсказать факт пролонгации страхового полиса (КАСКО для автомобиля).
Задача - создать API для модели. Качеству метрик модели особого внимания не уделялось.

В рамках задания сделано:
- обучено две модели - линейная регрессия и Xgboost, повторно обучить модели можно запустив скрипт `train_models.py`
- сделано API для этих моделей:
    - `http://127.0.0.1:5000/predict_logreg`
    - `http://127.0.0.1:5000/predict_xgboost`
- flask сервер "завернут" в докер, можно запустить через
   docker-compose up
- сервер также развернут на heroku:
[https://auto-insurance-churn-api.herokuapp.com/](https://auto-insurance-churn-api.herokuapp.com/)  
- для проверки API сделан скрипт: 
    - проверить локально - `python api_check.py`
    - проверить с heroku - `python api_check.py https://auto-insurance-churn-api.herokuapp.com/`  


### Распишите языки программирования и фреймворки, а также технологии, которые вы использовали в рамках создания проекта и для чего
- python
- pandas, sklearn, xgboost, joblib - обработка данных, обучение модели, сохранение и загрузка модели
- flask - создание API
- requests - проверка API
- gunicorn - сервер приложения
- pipenv - управление зависимостями в python
- docker/docker-compose - для деплоя
- heroku - для хостинга

### Продемонстрируйте работу проекта

[Видео демонстрация проекта](https://youtu.be/2Cmv5eyWH58)

### Распишите кратко по шагам процесс работы программы
**app.py**

    - Сервис загружает сохраненнию модель из pickle-файла
    - Примимает POST-запрос c данными клиента для анализа
    - Данные преобразуются из json в pandas dataframe
    - Происходит предобработка данных в модуле preproc
    - Данные попадают в модель и происходит расчет прогноза пролонгации полиса клиента
    - Результат расчета отдается ввиде json в ответе сервера на изначальный POST-запрос
    
**train.py**

    - Загружает датасет для обучения из папки data
    - Происходит предобработка данных в модуле preproc
    - Датасет разбирается на части для обучения и валидации
    - Обучаются две модели (линейная регрессия и Xgboost)
    - Вычисляются метрики модели (accuracy)
    - Модели сохраняются в pickle файлы

**api_check.py**

    - При вызове скрипта проверяются аргументы командной строки, если задан url, что запросы идут к нему, а не локально
    - Берется рандомная запись с сведениями о клиенте и отправляется POST запрос на два эндпойнта API сервера
    - Вывод на экран результатов запросов

### Как запустить вашу программу?
Установка и запуск сервера:
 
#### Основной способ (через докер):
```shell script
docker-compose up
```
Либо можно создать виртуальное окружение с python и зависимостями с помощью [pipenv](https://github.com/pypa/pipenv):
```sh
pipenv install
pipenv shell

# И потом запустить сервер

gunicorn --bind 127.0.0.1:5000 app:app
```

#### Протестировать работу API можно с помощью скрипта:
```shell script
python api_check.py
```

Либо можно в ручную отправить запрос (например, через Postman) на один из двух эндпоинтов:
```
http://127.0.0.1:5000/predict_logreg
http://127.0.0.1:5000/predict_xgboost
```
Пример json запроса:
```json
[
  {
    "POLICY_ID":96457,
    "POLICY_BEGIN_MONTH":8,
    "POLICY_END_MONTH":8,
    "POLICY_SALES_CHANNEL":52,
    "POLICY_SALES_CHANNEL_GROUP":6,
    "POLICY_BRANCH":"Санкт-Петербург",
    "POLICY_MIN_AGE":41,
    "POLICY_MIN_DRIVING_EXPERIENCE":0,
    "VEHICLE_MAKE":"Ford",
    "VEHICLE_MODEL":"Kuga",
    "VEHICLE_ENGINE_POWER":150.0,
    "VEHICLE_IN_CREDIT":0,
    "VEHICLE_SUM_INSURED":950000.0,
    "POLICY_INTERMEDIARY":"509",
    "INSURER_GENDER":"M",
    "POLICY_CLM_N":"2",
    "POLICY_CLM_GLT_N":"1L",
    "POLICY_PRV_CLM_N":"N",
    "POLICY_PRV_CLM_GLT_N":"N",
    "CLIENT_HAS_DAGO":0,
    "CLIENT_HAS_OSAGO":0,
    "POLICY_COURT_SIGN":0,
    "CLAIM_AVG_ACC_ST_PRD":0.0,
    "POLICY_HAS_COMPLAINTS":0,
    "POLICY_YEARS_RENEWED_N":"0",
    "POLICY_DEDUCT_VALUE":10000.0,
    "CLIENT_REGISTRATION_REGION":"Санкт-Петербург",
    "POLICY_PRICE_CHANGE":0.43
  }
]
```

Пример успешного ответа сервера («1» – клиент пролонгировался, «0» - клиент не пролонгировался):
```json
{"prediction": [1]}
```
