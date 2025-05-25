from fastapi import HTTPException, Security, status
from typing import Dict, Optional

from app.core.security import verify_token
from app.db import users

def get_user_from_sub(sub: str) -> Optional[Dict]:
    for user in users:
        if user.get("sub") == sub:
            return user
    return None

def get_optional_user(
    payload: Optional[Dict] = Security(verify_token),
) -> Optional[Dict]:
    """
    Retrieve the optional user payload from the security token.
    This dependency attempts to extract the user payload using the `verify_token` security scheme.
    If the token is not present or invalid, it returns None.
    Args:
        payload (Optional[Dict]): The user payload extracted from the security token, or None if not available.
    Returns:
        Optional[Dict]: The user payload dictionary if present, otherwise None.
    """
    
    if payload is None:
        return None
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    user = get_user_from_sub(sub=sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


def get_current_user(payload: Dict = Security(verify_token)) -> Dict:
    """
    Retrieve the current authenticated user from the provided token payload.
    This dependency function uses the `verify_token` security scheme to extract and validate
    the user's authentication token. If the token is valid, the corresponding payload (user data)
    is returned. If the token is missing or invalid, an HTTP 401 Unauthorized exception is raised.
    Args:
        payload (Dict): The decoded token payload containing user information, provided by the `verify_token` dependency.
    Returns:
        Dict: The payload containing authenticated user information.
    Raises:
        HTTPException: If authentication is missing or invalid, with status code 401.
    """

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires Authentication."
        )
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    user = get_user_from_sub(sub=sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
