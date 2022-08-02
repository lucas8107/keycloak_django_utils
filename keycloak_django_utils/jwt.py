import json
from dataclasses import dataclass, fields

import requests
import jwt

from django.core.cache import cache
from django.conf import settings


@dataclass
class TokenHeader:
    alg: str = None
    typ: str = None
    kid: str = None


def get_keycloak_public_key(key_id: str):
    json_key = cache.get(key_id)

    if not json_key:
        url = settings.KEYCLOAK_JWKS_ENDPOINT

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        json_key = json.dumps(
            next(filter(lambda item: item["kid"] == key_id, data.get("keys", [])), None)
        )
        cache.set(key_id, json_key)

    return jwt.api_jwk.PyJWK.from_json(json_key).key


def get_token_header(access_token: str):
    header = jwt.get_unverified_header(access_token)
    field_names = [i.name for i in fields(TokenHeader)]
    return TokenHeader(**{k: v for k, v in header.items() if k in field_names})


def validate_token(access_token: str, audience="account"):
    token_header = get_token_header(access_token)
    public_key = get_keycloak_public_key(token_header.kid)
    return jwt.decode(
        access_token, key=public_key, algorithms=token_header.alg, audience=audience
    )
