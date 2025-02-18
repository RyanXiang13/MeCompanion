from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from models import db, JournalEntry
from auth import register, login, protected
from nlp_utils import analyze_sentiment, generate_response

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

# Routes
app.route('/register', methods=['POST'])(register)
app.route('/login', methods=['POST'])(login)
app.route('/protected', methods=['GET'])(protected)

@app.route('/analyze', methods=['POST'])
@jwt_required()
def analyze():
    data = request.json
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    sentiment = analyze_sentiment(user_input)
    response = generate_response(user_input)

    # Save journal entry to database
    current_user_id = get_jwt_identity()
    new_entry = JournalEntry(text=user_input, sentiment=str(sentiment), user_id=current_user_id)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({
        "sentiment": sentiment,
        "response": response
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)