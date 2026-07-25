from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fast Food Express</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; text-align: center; }
        header { background-color: #e63946; color: white; padding: 20px; font-size: 24px; font-weight: bold; }
        .container { padding: 20px; }
        .card { background: white; border-radius: 10px; padding: 15px; margin: 15px auto; max-width: 300px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .btn { background-color: #ffb703; color: #000; border: none; padding: 10px 15px; border-radius: 5px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <header>🍔 Fast Food Express</header>
    <div class="container">
        <h2>¡Bienvenido a nuestro menú!</h2>
        <div class="card">
            <h3>Combo Hamburguesa</h3>
            <p>Hamburguesa doble con queso + Papas + Bebida</p>
            <button class="btn">Pedir ahora</button>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run()
