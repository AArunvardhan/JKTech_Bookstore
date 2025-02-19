from datetime import timedelta
from JKTech_Project.JKTech_Bookstore.my_bookstore.utils import create_access_token
from JKTech_Project.JKTech_Bookstore.my_bookstore.constants import SECRET_KEY, ALGORITHM
import jwt

def test_create_access_token():
    """Test token creation utility"""
    data = {"sub": "testuser"}
    token = create_access_token(data)
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded["sub"] == "testuser"
    assert "exp" in decoded

def test_create_access_token_with_expiry():
    """Test token creation with custom expiry"""
    data = {"sub": "testuser"}
    expires_delta = timedelta(minutes=30)
    token = create_access_token(data, expires_delta)
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded["sub"] == "testuser"