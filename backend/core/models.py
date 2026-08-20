from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    hashed_password: str
    role: str
    is_active: bool
