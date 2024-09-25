from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>NutriVida Rural</title>
        </head>
        <body>
            <h1>Bienvenidos a NutriVida Rural</h1>
            <p>Nuestra misión es eliminar la malnutrición en comunidades rurales desatendidas.</p>
            <a href='/productos'>Ver nuestros productos</a><br>
            <a href='/contacto'>Contáctanos</a>
        </body>
    </html>
    """

@app.route('/productos')
def productos():
    return """
    <html>
        <head>
            <title>Productos - NutriVida Rural</title>
        </head>
        <body>
            <h1>Productos de NutriVida Rural</h1>
            <ul>
                <li>Barras energéticas</li>
                <li>Leche en polvo fortificada</li>
                <li>Suplementos alimenticios</li>
            </ul>
            <a href='/'>Volver a la página principal</a>
        </body>
    </html>
    """

@app.route('/contacto')
def contacto():
    return """
    <html>
        <head>
            <title>Contacto - NutriVida Rural</title>
        </head>
        <body>
            <h1>Contáctanos</h1>
            <p>Para más información, escríbenos a contacto@nutrivida.com</p>
            <a href='/'>Volver a la página principal</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
