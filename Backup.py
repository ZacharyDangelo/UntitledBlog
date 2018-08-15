import os, shutil, gzip
import datetime as dt


def backup_database(db_conn, file_name):  #Basic database backup
    # log -- beginning database backup.
    file_name = os.path.join(os.getcwd(),file_name)
    backup_path = os.path.join(os.getcwd(), 'backups')

    try:
        os.makedirs(backup_path)
    except FileExistsError:
        pass

    backup_file = str(dt.date.today())+'DBBackup.json'
    backup_path = os.path.join(backup_path,backup_file)
    resulting_file = shutil.copy(file_name,backup_path)
    compress_file(resulting_file)
    # log -- database backup completed.


def compress_file(file_name):
    with open(file_name, 'rb') as f_in:
        with gzip.open(file_name +'.gz','wb') as f_out:
            shutil.copyfileobj(f_in,f_out)
    os.remove(file_name)



