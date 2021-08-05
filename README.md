#### Зайти в venv:
```shell
source venv/bin/activate
```
#### Установка зависимостей для venv:
```shell
pip3 install -r requirements.txt
```

#### Запуск сервера (0.0.0.0:7777)
```shell
uvicorn app.main:app --host 0.0.0.0 --port 7777 --reload
```