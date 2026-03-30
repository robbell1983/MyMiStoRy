import os
from flask import Flask, jsonify, request
from transformers import pipeline

# Serve il front-end compilato da Vite in dist/
app = Flask(__name__, static_folder="dist", static_url_path="")

# Inizializza il modello AI (opzionale, solo se usi endpoint /query)
nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Serve index.html generato dalla build Vite
@app.route("/")
def index():
    return app.send_static_file("index.html")

# Serve risorse statiche dalla cartella dist
@app.route("/<path:path>")
def static_proxy(path):
    return app.send_static_file(path)

# Endpoint del modello AI (facoltativo)
@app.route("/query", methods=["POST"])
def query_ai():
    data = request.json
    tema = data.get("tema", "")
    result = nlp(tema, candidate_labels=["scrittore", "musicista", "filosofo", "politico", "artista", "evento storico"])
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
