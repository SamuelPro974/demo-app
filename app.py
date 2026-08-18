#!/usr/bin/env python3
"""Application web de démonstration pour le TP d'automatisation DevOps.

Trois routes suffisent pour valider un déploiement :
  /            page d'accueil
  /health      sonde de santé (utilisée par le script de déploiement)
  /api/version version déployée (injectée par Docker via APP_VERSION)
"""
import os

from flask import Flask, jsonify

app = Flask(__name__)

# La version vient d'une variable d'environnement passée par docker run :
# on sait ainsi immédiatement quel commit tourne dans le conteneur.
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def home():
    return f"<h1>Application de démonstration</h1><p>Version : {VERSION}</p>"


@app.route("/health")
def health():
    """Renvoie 200 si l'application est opérationnelle."""
    return jsonify(status="ok", version=VERSION), 200


@app.route("/api/version")
def version():
    return jsonify(version=VERSION), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
