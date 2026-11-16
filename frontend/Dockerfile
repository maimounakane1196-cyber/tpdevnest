# 1. Image de départ : Node.js léger
FROM node:22-slim

# 2. Dossier de travail dans l'image
WORKDIR /app

# 3. Copier d'abord les fichiers de dépendances (pour profiter du cache Docker)
COPY package*.json ./

# 4. Installer les bibliothèques
RUN npm install

# 5. Copier tout le reste du code
COPY . .

# 6. Port utilisé par le frontend
EXPOSE 3000

# 7. Lancer l'application (--host 0.0.0.0 pour être accessible hors du conteneur)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]