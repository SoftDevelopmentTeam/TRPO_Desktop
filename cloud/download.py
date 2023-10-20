from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Авторизация
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Создаем объект GoogleDrive
drive = GoogleDrive(gauth)

# Указываем путь к папке, куда будут скачиваться файлы
local_folder_path = 'FileDownload'
drive_folder_name = 'root'

# Получаем список файлов в корневой папке Google Диска
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# Создаем папку для загрузки файлов
os.makedirs(local_folder_path, exist_ok=True)

# Скачиваем файлы
for file in file_list:
    if file['title'] == drive_folder_name:
        continue  # Пропускаем папку с тем же именем
    local_file_path = os.path.join(local_folder_path, file['title'])
    file.GetContentFile(local_file_path)

print(f'Скачано {len(file_list)} файлов в {local_folder_path}.')
