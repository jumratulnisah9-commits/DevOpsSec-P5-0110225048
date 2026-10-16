from app.storage import TaskStorage
from app.tasks import format_task


def main():
    storage = TaskStorage()

    while True:
        print("\n=== SecureTaskApp ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Tandai tugas selesai")
        print("4. Hapus tugas")
        print("5. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            title = input("Judul tugas: ")
            try:
                task = storage.add(title)
                print("Tugas ditambahkan:", format_task(task))
            except ValueError as error:
                print("Kesalahan:", error)

        elif choice == "2":
            tasks = storage.list_all()
            if not tasks:
                print("Belum ada tugas.")
            for task in tasks:
                print(format_task(task))

        elif choice == "3":
            try:
                task_id = int(input("ID tugas: "))
                task = storage.complete(task_id)
                print("Tugas diperbarui:", format_task(task))
            except ValueError:
                print("ID harus berupa angka.")
            except KeyError as error:
                print(error)

        elif choice == "4":
            try:
                task_id = int(input("ID tugas: "))
                storage.delete(task_id)
                print("Tugas berhasil dihapus.")
            except ValueError:
                print("ID harus berupa angka.")
            except KeyError as error:
                print(error)

        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()