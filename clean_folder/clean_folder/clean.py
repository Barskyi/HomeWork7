import os
import sys
from pathlib import Path
import glob


""" Створюємо список для файлів та папок які нас цікавлять """

pictures = list()
video = list()
doc = list()
sound = list()
archive_files = list()
other_files = list()  # не можемо визначити розширення
folders = list('pictures' 'video' 'doc' 'sound' 'archive_files')  # папки
unknowns = set()  # невідомі файли
extensions = set()  # відомі файли з якими ми працюємо

register_extension = {
    "JPEG": pictures,
    "PNJ": pictures,
    "JPL": pictures,
    "SVG": pictures,
    "AVI": video,
    "MP4": video,
    "MOV": video,
    "MKV": video,
    "DOC": doc,
    "DOCX": doc,
    "TXT": doc,
    "PDF": doc,
    "XLSX": doc,
    "PPTX": doc,
    "MP3": sound,
    "OGG": sound,
    "WAV": sound,
    "AMR": sound,
    "ZIP": archive_files,
    "GZ": archive_files,
    "TAR": archive_files,

}

def sorted_file(folder_path):
    """ Sorted our file into list and folders """
    for el in folder_path.iterdir():
        if el.is_file():
            for key in register_extension.keys():
                if str(el.suffix.replace('.', '')) in register_extension.keys():
                    other_files.append(el)
                    if str(el.suffix.replace('.', '')) == key:
                        register_extension[key].add(str(el.suffix.replace('.', '')))
                else:
                    unknowns.add(str(el.suffix.replace('.', '')))
        else:
            sorted_file(el)


UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
    "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    """ Підміна літер """

    TRANS[ord(key)] = value  # for little word
    TRANS[ord(key.upper())] = value.upper()  # for big word


def normalize(name):  # все що не невідоме заміняємо на " __ "

    """ Підміна символів """
    new_file_name = name.translate(TRANS)
    other_files_name = ''
    for i in new_file_name:
        if i.isalnum() or i == '.':
            other_files_name += i
        else:
            i = "_"
            other_files_name += i
    return other_files_name


def scan_file(folder_path):
    """ here we scan the files and  add them to the list """
    path = str(folder_path)
    for el in register_extension.keys():
        for file in glob(path + f'\\**\\*.{el}', recursive=True):
            register_extension[el].append(file)
            extensions.add(f'{el}')
        for file in glob(path + '\\**\\*.*', recursive=True):
            if not str(file.endswith(str(el))):
                other_files.append(file)
                unknowns.add(file[file.rindex('.') + 1:])


def empty_dir(path):
    try:
        for el in os.listdir(path):
            q = os.path.join(path, el)
            if os.path.isdir(q):
                empty_dir(q)
                if not os.listdir(q):
                    os.rmdir(q)
    except PermissionError:
        print("do re mi do re do - sol fa mi re do !")


def main(folder_path):
    path = folder_path
    sorted_file(path)
    empty_dir(path)


def search_path():
    path = sys.argv[1]
    arg = Path(path)
    main((arg.resolve()))


if __name__ == '__main__':
    search_path()

