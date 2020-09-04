from abc import ABC, abstractmethod

from voluptuous import MultipleInvalid, Schema


class ABCRequest(ABC):
    @classmethod
    @abstractmethod
    def _get_validation_schema(cls) -> Schema:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def from_dict(cls, dict_):
        raise NotImplementedError()


class BaseRequest(ABCRequest):
    @classmethod
    def _get_validation_schema(cls) -> Schema:
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, dict_):
        try:
            cls._get_validation_schema()(dict_)
        except MultipleInvalid as exception:
            print(exception)
            raise exception

        # noinspection PyArgumentList
        return cls(**dict_)
