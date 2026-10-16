import pytest

from app.tasks import create_task, complete_task
from app.storage import TaskStorage


def test_create_task():
    task = create_task("Belajar Python", 1)

    assert task["title"] == "Belajar Python"
    assert task["completed"] is False


def test_empty_title_is_rejected():
    with pytest.raises(ValueError):
        create_task("   ", 1)


def test_complete_task():
    task = create_task("Belajar DevSecOps", 1)
    updated = complete_task(task)

    assert updated["completed"] is True
    assert task["completed"] is False


def test_storage_add_and_delete():
    storage = TaskStorage()
    task = storage.add("Mengerjakan laporan")

    assert len(storage.list_all()) == 1

    storage.delete(task["id"])

    assert storage.list_all() == []