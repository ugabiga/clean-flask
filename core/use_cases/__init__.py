from abc import ABC, abstractmethod
from typing import Any


class BaseUseCase(ABC):
    @abstractmethod
    def execute(self) -> Any:
        raise NotImplementedError()
