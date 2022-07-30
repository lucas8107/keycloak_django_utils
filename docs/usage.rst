=====
Usage
=====

.. role:: python(code)
   :language: python

To use Keycloak Django Utils in a project

Set the variable KEYCLOAK_JWKS_ENDPOINT on your django settings. This is the keycloak keys endpoint (ends like "openid-connect/certs")

Authentication::

    from keycloak_django_utils.authentication import BearerAuthentication


Sets request.auth with the keycloak access_token validated info.

Permissions::

    from keycloak_django_utils.permissions import RolePermission
    from keycloak_django_utils.permissions import ServiceAccountPermission


You just need to extend :python:`RolePermission` or :python:`ServiceAccountPermission` and set the class variables :python:`has_client_roles` and :python:`has_realm_roles` with a list 
of the desired keycloak roles (list of strings). The role string follows the format::

    "<client_id>:<role_name>"


The :python:`ServiceAccountPermission` is similar to :python:`RolePermission` but if the access_token does not belong to a service account, then it is not permitted.