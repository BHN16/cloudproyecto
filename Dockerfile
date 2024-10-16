FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BOT_TOKEN="7217499827:AAG3cWTOrjlozGCIRJH7yOVx4Gc0FY5TvQM"

# Run the bot
CMD ["python", "bot.py"]