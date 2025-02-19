from datetime import datetime, timedelta, timezone

import jwt

from JKTech_Project.JKTech_Bookstore.my_bookstore.constants import ALGORITHM, SECRET_KEY


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Updated
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Updated
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
