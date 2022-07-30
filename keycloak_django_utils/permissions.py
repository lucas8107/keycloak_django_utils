from typing import Dict, Set
from rest_framework.request import Request
from rest_framework.permissions import BasePermission


def check_client_roles(roles_to_verify: Set, resource_access: Dict):
    _client_roles = set(roles_to_verify)
    for client_id, roles_obj in resource_access.items():
        _client_roles = _client_roles - {f"{client_id}:{role}" for role in (roles_obj.get("roles", []))}
    return not bool(_client_roles)


def check_realm_roles(roles_to_verify: Set, realm_access: Dict):
    _realm_roles = set(roles_to_verify)

    realm_roles = set(realm_access.get("roles", []))
    _realm_roles = _realm_roles - realm_roles
    return not bool(_realm_roles)


class RolePermission(BasePermission):
    has_realm_roles = []
    has_client_roles = []

    def has_permission(self, request: Request, view):
        token_info = request.auth

        has_client_roles_permissions = check_client_roles(self.has_client_roles, token_info.get("resource_access", {}))
        has_realm_roles_permissions = check_realm_roles(self.has_realm_roles, token_info.get("realm_access", {}))

        return has_client_roles_permissions and has_realm_roles_permissions



class ServiceAccountPermission(RolePermission):

    def has_permission(self, request: Request, view):
        token_info = request.auth

        if "clientId" not in token_info:
            return False

        if not token_info["preferred_username"].startswith("service-account"):
            return False
        
        return super().has_permission(request, view)
        