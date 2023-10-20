from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Авторизация
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Откроет окно браузера для авторизации

# Создаем объект GoogleDrive
drive = GoogleDrive(gauth)

# Создаем файл в корневой папке
#file1 = drive.CreateFile({'title': 'Пример.txt'})
#file1.Upload()

#print('Файл создан с id:', file1.get('id'))

# Получаем список файлов
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# Выводим информацию о файлах
print("Список файлов:")
for file in file_list:
    print('Название: %s, ID: %s' % (file['title'], file['id']))