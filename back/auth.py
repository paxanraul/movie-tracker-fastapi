import os
from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

# Контекст для хеширования. bcrypt — стандарт индустрии для паролей.
# Хеш получается медленный специально — чтобы перебор паролей был дорогим
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Секретный ключ для подписи JWT. На проде ОБЯЗАТЕЛЬНО через переменную окружения,
# чтобы не светить в коде. Если переменной нет — используем заглушку (только для разработки)
SECRET_KEY = os.getenv("JWT_SECRET", "dev-secret-change-me")

# Алгоритм подписи. HS256 — симметричный, один и тот же ключ и шифрует, и проверяет
ALGORITHM = "HS256"

# Срок жизни токена. 60 минут — разумный компромисс
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str):
    # Получить хеш пароля. Этот хеш кладём в БД.
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Проверить, что пароль соответствует хешу. Используется при логине.
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: int) -> str:
    # Создать JWT-токен для юзера. Внутри лежит user_id и время истечения.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id), # subject = кому выдан токен. JWT-стандарт требует строку
        "exp": expire # exp = expiration time. Библиотека сама проверит срок
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> int | None:
    """
    Расшифровать токен и вернуть user_id.
    Если токен невалиден или просрочен — вернёт None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        return int(user_id) if user_id else None
    except jwt.PyJWTError:
        return None