FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888
WORKDIR /usr/src/app/telegram_bot
CMD [ "python", "main.py" ]
