def validate_title(title):
    """Memastikan judul tugas valid."""
    if not isinstance(title, str):
        raise ValueError("Judul harus berupa teks.")

    title = title.strip()

    if not title:
        raise ValueError("Judul tugas tidak boleh kosong.")

    if len(title) > 100:
        raise ValueError("Judul maksimal 100 karakter.")

    return title