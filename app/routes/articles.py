import json
from datetime import datetime
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.articles import Article
from app.models import storage
from app.routes import articles_bp
from app.utils.date_time import format_datetime
from app.services.rate_limiter import rate_limit


# Get all articles by topic
@articles_bp.route("/articles/<topic>", methods=["GET"])
@jwt_required()
def get_articles_by_topic(topic):
    """Get all articles for a specific topic."""
    articles = storage.all(Article)
    topic_articles = [
        article.to_dict() for article in articles if article.topic == topic
    ]

    # Sort articles by publication date
    topic_articles.sort(key=lambda x: x["published_at"], reverse=True)
    return jsonify(topic_articles), 200


# Get all articles
@articles_bp.route("/articles", methods=["GET"])
@jwt_required()
def get_all_articles():
    """Retrieve all articles."""
    articles = storage.all(Article)
    all_articles = [article.to_dict() for article in articles]

    # Sort articles by publication date
    all_articles.sort(key=lambda x: x["published_at"], reverse=True)
    return jsonify(all_articles), 200


# Post a new article
@articles_bp.route("/articles", methods=["POST"])
@jwt_required()
# @rate_limit(limit=5, per=60)  # Limit to 5 articles per minute
def post_article():
    """Create a new article."""
    user_id = get_jwt_identity()
    data = request.json
    print(data)

    # Validate required fields
    required_fields = ["title", "author", "content", "published_at", "topic"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

        # Create and save new article
    article = Article(
        title=data["title"],
        author=data["author"],
        description=data.get("description", ""),
        content=data["content"],
        published_at=datetime.strptime(
            data["published_at"], "%Y-%m-%dT%H:%M:%S"),
        source=data.get("source", ""),
        url=data.get("url", ""),
        url_to_image=data.get("url_to_image", ""),
        topic=data["topic"],  # Define the article's topic
    )
    article.save()

    return jsonify({"message": "Article created successfully"}), 201


# Get a specific article by ID
@articles_bp.route("/articles/<article_id>", methods=["GET"])
@jwt_required()
def get_article(article_id):
    """Retrieve a single article by its ID."""
    article = storage.get(Article, article_id)
    if not article:
        return jsonify({"error": "Article not found"}), 404

    return jsonify(article.to_dict()), 200
