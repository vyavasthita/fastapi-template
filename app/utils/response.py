from typing import Any
from dataclasses import dataclass


@dataclass
class Response:
    is_success: bool = True
    message: str = None
    result: Any = None
