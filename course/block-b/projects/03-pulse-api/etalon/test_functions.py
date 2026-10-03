from functions import top3, validate_score


def test_top3_order():
    data = [
        {"title": "b", "plays": 1},
        {"title": "a", "plays": 5},
        {"title": "c", "plays": 5},
        {"title": "d", "plays": 2},
    ]
    result = top3(data)
    assert [t["title"] for t in result] == ["a", "c", "d"]


def test_validate_rejects_negative():
    assert validate_score({"name": "Ada", "score": -1})
