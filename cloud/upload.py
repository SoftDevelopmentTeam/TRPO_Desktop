from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Авторизация
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Создаем объект GoogleDrive
drive = GoogleDrive(gauth)

# Указываем путь к папке с файлами
local_folder_path = 'FileUpToDrive'

# Получаем список файлов в локальной папке
local_files = os.listdir(local_folder_path)

# Загружаем файлы на Google Диск
for file_name in local_files:
    file_path = os.path.join(local_folder_path, file_name)
    drive_file = drive.CreateFile({'title': file_name, 'parents': [{'id': 'root'}]})
    drive_file.Upload()

print(f'Загружено {len(local_files)} файлов на Google Диск.')
