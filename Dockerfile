# Basis-Image mit Python
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Abhängigkeiten zuerst kopieren (Cache-Vorteil)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Projektdateien kopieren
COPY . .

# Flask-Umgebungsvariablen
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Port freigeben
EXPOSE 5000

# App starten
CMD ["python", "main.py"]

# GitHub Packages Metadaten (Teilaufgabe 2)
LABEL org.opencontainers.image.source https://github.com/Smileyfish/zu-bbbearbeiten-stateless

