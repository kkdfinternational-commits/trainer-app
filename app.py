from flask import Flask
from forms import forms_bp
from admin import admin_bp
from trainer import trainer_bp

app = Flask(__name__)
app.secret_key = "kkdf_secret"

app.register_blueprint(forms_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(trainer_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
