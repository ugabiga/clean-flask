from abc import ABC

from app.core.entities.authentication import Authentication as AuthenticationEntity


class AuthenticationRepository(ABC):
    def create_auth(self, auth: AuthenticationEntity) -> AuthenticationEntity:
        raise NotImplementedError()