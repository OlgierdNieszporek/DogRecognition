# wykorzystujemy obraz oficjalny Python 3.8 z repozytorium Docker Hub
FROM python:3.8-slim-buster

# aktualizujemy system i instalujemy wymagane pakiety
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libjpeg-dev libpng-dev && \
    rm -rf /var/lib/apt/lists/*

# ustawiamy katalog roboczy
WORKDIR /app

# kopiujemy pliki aplikacji do kontenera
COPY . .

# instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# ustawiamy zmienną środowiskową dla portu
ENV PORT=5000

# nasłuchujemy na porcie zdefiniowanym przez zmienną środowiskową
CMD gunicorn --bind 0.0.0.0:$PORT main:app