from passlib.context import CryptContext
import random
import string
from app.utils.response import Response
    

class PasswordGenerator:
    def __init__(self, length: int = 10) -> None:
        self._length = length
        self._lower = string.ascii_lowercase
        self._upper = string.ascii_uppercase
        self._num = string.digits
        self._symbols = string.punctuation

    def generate_password(self) -> Response:
        password = None

        try:
            all = self._lower + self._upper + self._num + self._symbols
            password = "".join(random.sample(all, self._length))
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
        
    def gen_hash_password(self, password) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, password, hash_password) -> bool:
        return self.pwd_context.verify(password, hash_password)
