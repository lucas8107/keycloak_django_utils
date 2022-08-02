from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException, status

from keycloak_django_utils.jwt import validate_token


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Incorrect authentication credentials."
    default_code = "authentication_failed"


class BearerAuthentication(TokenAuthentication):
    keyword = "Bearer"
    audience = "account"

    def authenticate_credentials(self, key):
        try:
            validated_token_info = validate_token(key, audience=self.audience)
        except Exception as e:
            raise AuthenticationFailed(detail=str(e))
        return None, validated_token_info
