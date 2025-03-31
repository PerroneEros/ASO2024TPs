from flask import Flask
from rutas.rutas_libro import libros_bp

app = Flask(__name__)
# Registrar el "blueprint" en la aplicación
app.register_blueprint(libros_bp)

if __name__ == '__main__':
    app.run()