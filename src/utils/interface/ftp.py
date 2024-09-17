"""  интерейс взаимодействия с файлами по протоку `FTP`
@details Я могу отправлять и получать файлы от моего сервера. Зачем? А как отправлять медиа (картинки, видео), файлы таблиц и прочие,
действия с файлом

 
 @section libs imports:
  - helpers (local)
  - typing 
  - ftplib 
  - pathlib 
  
"""

## \file ../src/utils/interface/ftp.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from src.logger import  logger
from typing import Union

import ftplib
from pathlib import Path


#_connection: dict = {'server': connection_ftp['server'],
#                     'port': connection_ftp['server'],
#                     'user': connection_ftp['server'],
#                     'password': connection_ftp['password']}


def send(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
      Sends a file to an FTP server.  

         source_file_path : str : The path of the file to be sent.  
         dest_dir : str : The destination directory on the FTP server.  
         dest_file_name : str : The name of the file on the FTP server.  

         bool : True if the file is succesStringFormatterully sent, False otherwise.  
    """
    try:
        # Establish connection to FTP server
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)
    except Exception as ex:
        # Log error if connection to FTP server fails
        logger.error(f'''Failed to connect to FTP server. 
        Error: {ex.with_traceback(ex.__traceback__)}''')
        return

    try:
        # Open the file and send it to the FTP server
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}/', f)
        _ret = True
    except Exception as ex:
        # Log error if file tranStringFormatterer to FTP server fails
        logger.error(
            f'''Failed to send file to FTP server. 
            Error: {ex.with_traceback(ex.__traceback__)}''')
        _ret = False

    finally:
        try:
            # Close the FTP session
            session.quit()
        except:
            ...
        return _ret

def receive(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    ...