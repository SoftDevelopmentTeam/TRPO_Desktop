from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def connect_to_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def upload_file_to_drive(drive, local_file_path):
    file_drive = drive.CreateFile({'title': os.path.basename(local_file_path)})
    file_drive.Upload()
    return file_drive['id']

def download_all_files_from_drive(drive, local_folder_path):
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file_drive in file_list:
        local_file_path = os.path.join(local_folder_path, file_drive['title'])
        file_drive.GetContentFile(local_file_path)

def download_file_from_drive(drive, file_id, local_file_path):
    file_drive = drive.CreateFile({'id': file_id})
    file_drive.GetContentFile(local_file_path)

def list_files_in_drive(drive):
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file_drive in file_list:
        print(f'Имя файла: {file_drive["title"]}, ID: {file_drive["id"]}')

def main():
    drive = connect_to_google_drive()

    while True:
        action = input("Что вы хотите сделать? (u - загрузить, d - скачать, q - выход): ").strip()

        if action == 'u':
            api_upload_dir = os.path.join(os.getcwd(), 'api_upload')

            for root, dirs, files in os.walk(api_upload_dir):
                for file_name in files:
                    local_file_path = os.path.join(root, file_name)
                    file_id = upload_file_to_drive(drive, local_file_path)
                    print(f"Файл '{file_name}' успешно загружен. ID файла на Google Диске: {file_id}")

        elif action == 'd':
            download_option = input("Какие файлы вы хотите скачать? (a - все файлы, s - один конкретный файл): ").strip()

            if download_option == 'a':
                local_folder_path = os.path.join(os.getcwd(), 'api_down')  # Путь к папке api_down
                download_all_files_from_drive(drive, local_folder_path)
                print(f"Все файлы успешно скачаны.")

            elif download_option == 's':
                list_files_in_drive(drive)
                file_id = input("Введите ID файла для скачивания: ").strip()
                local_file_path = os.path.join(os.getcwd(), 'api_down', input("Введите имя файла для сохранения: "))
                download_file_from_drive(drive, file_id, local_file_path)
                print(f"Файл успешно скачан.")

            else:
                print("Неверная команда. Пожалуйста, введите 'a' для скачивания всех файлов или 's' для скачивания конкретного файла.")

        elif action == 'q':
            break

        else:
            print("Неверная команда. Пожалуйста, введите 'u' для загрузки, 'd' для скачивания или 'q' для выхода.")

if __name__ == "__main__":
    main()
