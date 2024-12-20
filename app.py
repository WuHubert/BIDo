from flask import Flask
from routes.config import API_CONFIG
from routes.image_routes import image_bp

app = Flask(__name__)
app.register_blueprint(image_bp)


if __name__ == '__main__':
    app.run(debug=True)