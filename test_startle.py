import pytest
from startle import generate_random_time, store_file, user_rating


def test_generate_random_time():
    assert len(generate_random_time(1)) == 4
    assert len(generate_random_time(2)) == 7


def test_store_file(tmp_path):
    test_list = [1, 2, 3, 4, 5]
    test_file = tmp_path / "test_history_file.txt"
    store_file(test_list, str(test_file))
    with open(test_file, "r") as f:
        content = f.read()
    assert "+----------+----------+----------+" in content
    assert "3" in content


def test_user_rating(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert user_rating() == "5"
    monkeypatch.setattr('builtins.input', lambda _: "7")
    assert user_rating() == "7"


