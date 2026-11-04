import os
import hashlib
import hmac

from class_models import LoginCheckPayload
from class_models import AuthPayload


    
def generate_password_hash(user_id: str, password: str) -> str:
    """Executes steps 2 through 5 to produce a hex-encoded PBKDF2 hash."""
    # Step 1: Retrieve the secret pepper from environment variables
    pepper = os.environ.get("SECRET_PEPPER")
    if not pepper:
        raise EnvironmentError("SECRET_PEPPER environment variable is not set.")

    # Step 2: Append the secret pepper to the password string
    peppered_password = password + pepper

    # Step 3: Hash using hashlib.pbkdf2_hmac with the user ID as the salt
    binary_hash = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=peppered_password.encode('utf-8'),
        salt=user_id.encode('utf-8'),
        iterations=1_048_576
    )

    # Step 4: Convert the binary hash output into a hexadecimal string
    return binary_hash.hex()


def register_user(user_id: str, password: str, database: dict) -> str:
    #Step 5: For a new user, store the hexadecimal string in the database.
    hex_hash = generate_password_hash(user_id, password)
    database[user_id] = hex_hash
    return hex_hash


def authenticate_user(user_id: str, password: str, database: dict) -> tuple[bool,str]:
    #Step 6: Re-compute hash and verify using hmac.compare_digest.
    stored_hash = database.get(user_id)
    if not stored_hash:
        return (False,"User Not There")

    # Repeat steps 1 through 5
    candidate_hash = generate_password_hash(user_id, password)

    # Compare in constant time to prevent timing attacks
    check = hmac.compare_digest(candidate_hash, stored_hash)
    if check:
        return(True , "login successful")
    else:
        return(False , "invalid password")
        
def process_login(payload: LoginCheckPayload, database: dict) -> AuthPayload:
    # Extract the values into separate variables
    user_id = payload.get("user_id",None)
    password = payload.get("password",None)
    role = payload.get("role",None)

    # If missing required credentials, immediately return unauthenticated payload
    if not user_id or not password:
        return AuthPayload(
            authenticated = False,
            reason = "Invalid Credentials",
            user_id=None,
            ban_status=False
        )

    # Check authentication against database
    (is_authenticated,reason_for_fail_pass) = authenticate_user(user_id, password, database)

    # Return the AuthPayload TypedDict
    return AuthPayload(
        authenticated=is_authenticated,
        reason = reason_for_fail_pass,
        user_id=user_id if is_authenticated else None,
        ban_status=False
    )
