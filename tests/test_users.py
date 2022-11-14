from app.models import User


def test_password_setter():
    u = User(password='cat')
    assert u.password_hash is not None

def test_password_verification():
    u = User(password='cat')
    assert u.verify_password('cat') == True
    assert u.verify_password('dog') == False

def test_password_hash_are_random():
    u1 = User(password='cat')
    u2 = User(password='cat')
    assert u1.password_hash != u2.password_hash