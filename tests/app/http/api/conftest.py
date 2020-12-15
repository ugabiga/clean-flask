import pytest
from sqlalchemy.orm import scoped_session  # type:ignore

from core.repositories.tasks import TaskRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def task_repo(session: scoped_session) -> TaskRepository:
    return TaskRepository()
