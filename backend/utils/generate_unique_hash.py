import hashlib
import uuid


def generate_unique_hash() -> str:
    unique_id = str(uuid.uuid4())
    hashed_id = hashlib.sha256(unique_id.encode()).hexdigest()
    return hashed_id
