from pathlib import Path
import json

DATA = Path(__file__).parent / "data" / "scores.json"


def load_scores():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text(encoding="utf-8"))


def save_scores(rows):
    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def top3(tracks):
    return sorted(tracks, key=lambda t: (-t["plays"], t["title"]))[:3]


def validate_score(payload):
    name = str(payload.get("name", "")).strip()
    try:
        score = int(payload.get("score"))
    except (TypeError, ValueError):
        return "score must be int"
    if not name:
        return "name required"
    if len(name) > 40:
        return "name too long"
    if score < 0 or score > 9999:
        return "score out of range"
    return None
