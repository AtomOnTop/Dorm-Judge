import os
import hashlib
import hmac
from typing import TypedDict, Optional

# --- Mocked from class_models.py ---
class LoginCheckPayload(TypedDict, total=False):
    user_id: Optional[str]
    password: Optional[str]
    role: Optional[str]

class AuthPayload(TypedDict):
    authenticated: bool
    reason: str
    user_id: Optional[str]
    ban_status: bool


# --- Your Authentication Implementation ---
def generate_password_hash(user_id: str, password: str) -> str:
    """Executes steps 2 through 5 to produce a hex-encoded PBKDF2 hash."""
    pepper = os.environ.get("SECRET_PEPPER")
    if not pepper:
        raise EnvironmentError("SECRET_PEPPER environment variable is not set.")

    peppered_password = password + pepper

    binary_hash = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=peppered_password.encode('utf-8'),
        salt=user_id.encode('utf-8'),
        iterations=1_048_576
    )

    return binary_hash.hex()


def register_user(user_id: str, password: str, database: dict) -> str:
    hex_hash = generate_password_hash(user_id, password)
    database[user_id] = hex_hash
    return hex_hash


def authenticate_user(user_id: str, password: str, database: dict) -> tuple[bool, str]:
    stored_hash = database.get(user_id)
    if not stored_hash:
        return (False, "User Not There")

    candidate_hash = generate_password_hash(user_id, password)

    check = hmac.compare_digest(candidate_hash, stored_hash)
    if check:
        return (True, "login successful")
    else:
        return (False, "invalid password")


def process_login(payload: LoginCheckPayload, database: dict) -> AuthPayload:
    user_id = payload.get("user_id", None)
    password = payload.get("password", None)
    role = payload.get("role", None)

    if not user_id or not password:
        return AuthPayload(
            authenticated=False,
            reason="Invalid Credentials",
            user_id=None,
            ban_status=False
        )

    (is_authenticated, reason_for_fail_pass) = authenticate_user(user_id, password, database)

    return AuthPayload(
        authenticated=is_authenticated,
        reason=reason_for_fail_pass,
        user_id=user_id if is_authenticated else None,
        ban_status=False
    )


# --- Execution & Test Examples ---
if __name__ == "__main__":
    # Set the required environment variable
    os.environ["SECRET_PEPPER"] = "super_secret_server_pepper_99!"
    
    # In-memory mock database
    db = {}

    # 1. Register a user
    print("--- 1. Registering User 'alice' ---")
    alice_hash = register_user("alice", "CorrectHorseBatteryStaple", db)
    print(f"Database State: {db}\n")

    # 2. Example A: Valid Login
    print("--- 2. Test Valid Login ---")
    valid_payload: LoginCheckPayload = {
        "user_id": "alice",
        "password": "CorrectHorseBatteryStaple",
        "role": "admin"
    }
    print(process_login(valid_payload, db), "\n")

    # 3. Example B: Wrong Password
    print("--- 3. Test Wrong Password ---")
    wrong_pw_payload: LoginCheckPayload = {
        "user_id": "alice",
        "password": "WrongPassword123",
        "role": "admin"
    }
    print(process_login(wrong_pw_payload, db), "\n")

    # 4. Example C: Non-Existent User
    print("--- 4. Test Non-Existent User ---")
    unknown_user_payload: LoginCheckPayload = {
        "user_id": "bob",
        "password": "SomePassword",
        "role": "user"
    }
    print(process_login(unknown_user_payload, db), "\n")

    # 5. Example D: Missing / Empty Credentials
    print("--- 5. Test Missing Credentials ---")
    missing_cred_payload: LoginCheckPayload = {
        "user_id": "alice",
        "password": "",
        "role": "user"
    }
    print(process_login(missing_cred_payload, db))