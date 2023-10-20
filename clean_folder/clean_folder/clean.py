from pathlib import Path
import shutil

pictures = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'heic', 'tiff', 'ico', 'webp', 'JPG']
movie = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm', '3gp', 'm4v', 'ts', 'ogg']
documents = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'rtf']
audio = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a']
text_documents = ['txt', 'rtf', 'odt',  'md']
achives = ["zip", "gz", "tar", "dmg"]
python_learn = ["ipynb"]
trying_movie = []

class Way:
    def __init__(self, path):
        self.path = Path(path)

    def recursive_func(self, recursive):

        for i in recursive.iterdir():  # проходимось по всіх файлах у заданій директорії

            if i.is_dir():  # якщо це директорія
                self.recursive_func(i)  # викликаємо рекурсію що б ввійти в середину
            elif i.is_file():  # якщо це файл а не папка
                if i.suffix[1:].lower() in pictures:  # якщо фото
                    self.photo(i)
                elif i.suffix[1:].lower() in movie:  # якщо відео
                    self.movie(i)
                elif i.suffix[1:].lower() in documents:
                    self.documents(i)
                elif i.suffix[1:].lower() in audio:
                    self.audio(i)
                elif i.suffix[1:].lower() in text_documents:
                    self.text(i)
                elif i.suffix[1:].lower() in achives:
                    self.achivs(i)
                elif i.suffix[1:].lower() in python_learn:
                    self.python_files(i)
                else:
                    self.unknown(i)

    def photo(self, file):  # file приймає шлях з recursive_func
        work_photo = self.path / 'WORK_IMAGES'  # назва  нової дерикторії яку ми створюєм
        work_photo.mkdir(parents=True, exist_ok=True)  # для коректності даних
        shutil.move(file, work_photo / file.name)

    def movie(self, file):
        movies = self.path / 'MOVIE'
        movies.mkdir(parents=True, exist_ok=True)
        shutil.move(file, movies / file.name)
        trying_movie.append(str(file.name))

    def documents(self, file):
        document = self.path / "DOC - FILES"
        document.mkdir(parents=True, exist_ok=True)
        shutil.move(file, document / file.name)

    def audio(self, file):
        music = self.path / "MUSIC"
        music.mkdir(parents=True, exist_ok=True)
        shutil.move(file, music / file.name)  # file - це файл який до нас приходить з метода recursive_func

    def text(self, file):
        texts = self.path / "TEXTS"
        texts.mkdir(parents=True, exist_ok=True)
        shutil.move(file, texts / file.name)

    def unknown(self, files):
        unknowns = self.path / "UNKNOWN"
        unknowns.mkdir(parents=True, exist_ok=True)
        shutil.move(files, unknowns / files.name)

    def achivs(self, files):
        achive = self.path / "ARCHIVE"
        achive.mkdir(parents=True, exist_ok=True)
        shutil.move(files, achive / files.name)

    def python_files(self, files):
        pyth = self.path / "Python-Learn"
        pyth.mkdir(parents=True, exist_ok=True)
        shutil.move(files, pyth / files.name)

    def delete_empty_folders_recursive(self):
        for item in self.path.iterdir():
            if item.is_dir():
                subfolder = Way(item)
                subfolder.delete_empty_folders_recursive()
        if not any(self.path.iterdir()):
            try:
                self.path.rmdir()
            except OSError:
                pass

def main():
    way = Way("/Users/olenka1/Downloads")
    way.recursive_func(way.path)
    way.delete_empty_folders_recursive()


if __name__=="__main__":
    main()
