from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def home():
    return jsonify(
        {
            "app": "QuizGazer",
            "message": "QuizGazer is up. Start building routes for quizzes, facts, and daily questions here."
        }
    )
