# Использование официального образа Python как базового
FROM python:3.8

# Установка рабочего каталога в контейнере
WORKDIR /usr/src/app

# Копирование содержимого папки backend внутрь контейнера
COPY . .
#
# Копирование файла requirements.txt внутрь контейнера
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 80 для внешнего доступа
EXPOSE 80

# Указание команды для запуска приложения
CMD ["python", "./app.py"]
