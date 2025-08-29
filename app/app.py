from flask import Flask
from appdb import db
from routes.main_routes import main


app = Flask(__name__)
app.config.from_object("config.Config")

#INitialize DB
db.init_app(app)

#Register routes
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
