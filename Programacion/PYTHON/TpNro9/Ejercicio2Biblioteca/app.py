from flask import Flask
from rutas.rutas_socio import socios_bp

app = Flask(__name__)
# Registrar el "blueprint" en la aplicación
app.register_blueprint(socios_bp)

if __name__ == '__main__':
    app.run()