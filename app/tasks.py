from app.validators import validate_title


def create_task(title, task_id):
    """Membuat tugas baru."""
    return {
        "id": task_id,
        "title": validate_title(title),
        "completed": False,
    }


def complete_task(task):
    """Menandai tugas sebagai selesai."""
    updated_task = task.copy()
    updated_task["completed"] = True
    return updated_task


def format_task(task):
    """Mengubah tugas menjadi teks yang mudah dibaca."""
    status = "Selesai" if task["completed"] else "Belum selesai"
    return f'{task["id"]}. {task["title"]} - {status}'