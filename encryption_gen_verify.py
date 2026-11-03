from class_models import LoginCheckPayload

def process_login(payload: LoginCheckPayload):
    # Extract the values into separate variables
    user_id = payload.get("user_id")
    password = payload.get("password")
    role = payload.get("role")


