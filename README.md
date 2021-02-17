# simpleWebTemplate

Простой шаблон для Web проекта
>Шаблон содержит пример REST_API и документацию Swagger,
 так же реализована единая точка входа и возможность вызова метода переданного в JSON

## Подготовка среды

```
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv
pip install wheel
sudo ufw allow 5000


# Создаем виртуальную среду
cd ~/envs
python3.9 -m venv webtemplateflask
source webtemplateflaskenv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt
```

## Запуск
```
# Запускам для разработки
python service.py

# Запуск под gunicorn
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

## Просмотр API
[link](http://localhost:5000/api/doc/)

## Сбор и запуск в docker

```
docker build -t name_image .
docker run --rm -it -p 5000:5000 name_image

```