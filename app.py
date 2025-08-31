import os
from flask import Flask
from flask_migrate import Migrate
from api.api import routes
from database.database import db

# Crear la app
app = Flask(__name__)
app.config.from_object('config.Config')

# Inicializar base de datos
db.init_app(app)

# Inicializar migraciones
migrate = Migrate(app, db)

# Registrar blueprint con prefijo
app.register_blueprint(routes, url_prefix='/star')

# Ejecutar la app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=False)
