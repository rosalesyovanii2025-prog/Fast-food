from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "mensaje": "¡Servidor web desplegado y funcionando en Vercel!"
    })

if __name__ == '__main__':
    app.run()
