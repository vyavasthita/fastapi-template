from passlib.context import CryptContext
import random
import string
from app.utils.response import Response
    

class PasswordGenerator:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    @classmethod
    def generate_password(cls, length: int = 10) -> Response:
        password = None

        try:
            all = cls.lower + cls.upper + cls.num + cls.symbols
            password = "".join(random.sample(all, length))
        except Exception as err:
            return Response(
                is_success=False, 
                message="Failed to generate password. {}".format(str(err))
            )

        return Response(
            result=password
        )

class PasswordHash:
    pwd_context: str = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
    @classmethod
    def gen_hash_password(cls, password) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password, hash_password) -> bool:
        return cls.pwd_context.verify(password, hash_password)
