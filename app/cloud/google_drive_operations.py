from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


class GDrive:
    @staticmethod
    def connect_to_drive():
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        return drive

    @staticmethod
    def connect_to_folder(drive, folder_id):
        folder = drive.CreateFile({'id': folder_id})
        return folder

    @staticmethod
    def upload_file_to_drive(drive, local_file_path, folder):
        file_drive = drive.CreateFile({'title': os.path.basename(local_file_path), 'parents': [{'id': folder['id']}]})
        file_drive.Upload()

    @staticmethod
    def download_file_from_drive(drive, file_id, local_file_path):
        file_drive = drive.CreateFile({'id': file_id})
        file_drive.GetContentFile(local_file_path)

    @staticmethod
    def list_files_in_drive(drive, folder):
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder['id'])}).GetList()
        for index, file_drive in enumerate(file_list, 1):
            print('{} Имя файла: {}, ID: {}'.format(index, file_drive["title"], file_drive["id"]))
        return file_list


class Adapter:
    def __init__(self, g_drive):
        self.drive_obj = g_drive
        self.drive = self.drive_obj.connect_to_drive()
        self.folder = None

    def connect_to_folder(self, folder_id):
        self.folder = self.drive_obj.connect_to_folder(self.drive, folder_id)

    def upload_file_to_drive(self, local_file_path):
        self.drive_obj.upload_file_to_drive(self.drive, local_file_path, self.folder)

    def download_file_from_drive(self, file_id, local_file_path):
        self.drive_obj.download_file_from_drive(self.drive, file_id, local_file_path)

    def list_files_in_drive(self):
        return self.drive_obj.list_files_in_drive(self.drive, self.folder)
