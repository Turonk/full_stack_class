from app import app


def test_health():
    client = app.test_client()
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json()["ok"] is True


def test_unknown_track():
    client = app.test_client()
    res = client.get("/api/tracks/nope")
    assert res.status_code == 404


def test_bad_score():
    client = app.test_client()
    res = client.post("/api/scores", json={"name": "Ada", "score": -3})
    assert res.status_code == 400
