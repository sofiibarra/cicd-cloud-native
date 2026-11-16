import os

from flask import Flask, jsonify

app = Flask(__name__)

MENSAJE = "Hola desde AWS Fargate - version 1"


def sumar(a, b):
    return a + b


@app.route("/")
def inicio():
    version = os.environ.get("APP_VERSION", "local")
    return (
        "<html><body style='font-family:Arial;text-align:center;margin-top:80px'>"
        f"<h1>{MENSAJE}</h1>"
        f"<p>Commit desplegado: <b>{version}</b></p>"
        "</body></html>"
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/sumar/<int:a>/<int:b>")
def ruta_sumar(a, b):
    return jsonify(resultado=sumar(a, b))
