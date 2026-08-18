# Image de base légère et officielle
FROM python:3.12-slim

WORKDIR /app

# On copie d'abord requirements.txt seul : tant qu'il ne change pas, Docker
# réutilise le cache de cette couche et le build est quasi instantané.
COPY requirements.txt .

# INSTALLATION DES DÉPENDANCES : elle a lieu DANS l'image, pas sur le serveur.
# --no-cache-dir : évite de stocker les archives pip (image plus légère).
RUN pip install --no-cache-dir -r requirements.txt

# Puis le code applicatif
COPY app.py .

# curl sert au health check interne de Docker
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

ENV PORT=3000
EXPOSE 3000

CMD ["python", "app.py"]
