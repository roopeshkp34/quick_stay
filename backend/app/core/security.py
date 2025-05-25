from typing import Dict, Optional

import jwt
from fastapi import Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, SecurityScopes

from app.core.config import settings

JWT_CLINT = jwt.PyJWKClient(settings.CLERK_JWKS_URL)
bearer_scheme = HTTPBearer(auto_error=False)

def decode_token(token: str):
    try:
        signing_key = JWT_CLINT.get_signing_key_from_jwt(token).key
        return jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            audience="https://content-beagle-76.clerk.accounts.dev",
            issuer=settings.CLERK_ISSUER,
            options={"verify_aud": False}
        )
    except (jwt.exceptions.DecodeError, jwt.exceptions.PyJWKClientError) as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_403_FORBIDDEN
        )
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            detail="Token has expired",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


def verify_token(
    security_scopes: SecurityScopes,
    token: Optional[HTTPAuthorizationCredentials] = Security(bearer_scheme),
) -> Dict:
    if token is None:
        return None

    decoded_payload = decode_token(token.credentials)
    return decoded_payload
