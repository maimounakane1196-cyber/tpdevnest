# 1. Image de départ : une image Python
FROM python:3.12-slim

# 2. Dossier de travail dans l'image
WORKDIR /app

# 3. Copier d'abord la liste des bibliothèques
COPY requirements.txt .

# 4. Installer les bibliothèques
RUN pip install -r requirements.txt

# 5. Copier le reste du code
COPY . .

# 6. Port utilisé par FastAPI (backend)
EXPOSE 8000

# 7. Lancer le serveur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]