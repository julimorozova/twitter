#### Зайти в venv:
```shell
source venv/bin/activate
```
#### Установка зависимостей для venv:
```shell
pip3 install -r requirements.txt
```

#### Запуск сервера (127.0.0.1:8000)
```shell
uvicorn app.main:app --reload
```