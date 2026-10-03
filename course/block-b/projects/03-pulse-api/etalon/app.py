from functools import wraps

from flask import Flask, jsonify, request, session
from flask_cors import CORS

from functions import load_scores, save_scores, top3, validate_score

app = Flask(__name__)
app.secret_key = "pulselab-dev-only"
CORS(app)

TRACKS = [
    {"id": "pixel", "title": "Pixel Tide", "artist": "Nova Park", "plays": 12},
    {"id": "battery", "title": "Low Battery", "artist": "Kite Club", "plays": 30},
    {"id": "bell", "title": "After Bell", "artist": "Школьный коридор", "plays": 21},
]


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("user"):
            return jsonify({"error": "need login"}), 401
        return fn(*args, **kwargs)

    return wrapper


@app.get("/api/health")
def health():
    return jsonify({"ok": True, "version": "2.0"})


@app.get("/api/tracks")
def tracks():
    return jsonify(TRACKS)


@app.get("/api/tracks/<track_id>")
def track_detail(track_id):
    found = next((t for t in TRACKS if t["id"] == track_id), None)
    if not found:
        return jsonify({"error": "not found"}), 404
    return jsonify(found)


@app.get("/api/top")
def top():
    return jsonify(top3(TRACKS))


@app.get("/api/scores")
def scores():
    data = sorted(load_scores(), key=lambda row: row["score"], reverse=True)[:10]
    return jsonify(data)


@app.post("/api/scores")
def add_score():
    payload = request.get_json(silent=True) or {}
    error = validate_score(payload)
    if error:
        return jsonify({"error": error, "field": "score"}), 400
    rows = load_scores()
    rows.append({"name": payload["name"].strip(), "score": int(payload["score"])})
    save_scores(rows)
    return jsonify({"ok": True}), 201


@app.post("/api/login")
def login():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    pin = str(payload.get("pin", ""))
    if not name or pin != "1234":
        return jsonify({"error": "bad login"}), 400
    session["user"] = name
    return jsonify({"user": name})


@app.post("/api/logout")
def logout():
    session.clear()
    return jsonify({"ok": True})


@app.get("/api/me")
def me():
    user = session.get("user")
    if not user:
        return jsonify({"user": None}), 200
    return jsonify({"user": user})


@app.get("/api/cabinet")
@login_required
def cabinet():
    return jsonify({"user": session["user"], "orders": []})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
