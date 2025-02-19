from JKTech_Project.JKTech_Bookstore.my_bookstore.middleware import JWTBearer
from JKTech_Project.JKTech_Bookstore.my_bookstore.constants import SECRET_KEY, ALGORITHM
import jwt

def test_jwt_bearer_valid_token():
    """Test JWTBearer with a valid token"""
    token = jwt.encode({"sub": "testuser"}, SECRET_KEY, algorithm=ALGORITHM)
    jwt_bearer = JWTBearer()
    assert jwt_bearer.verify_jwt(token) == True

def test_jwt_bearer_invalid_token():
    """Test JWTBearer with an invalid token"""
    jwt_bearer = JWTBearer()
    assert jwt_bearer.verify_jwt("invalid_token") == False