class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self._get_w_h()

    def __str__(self):  # Представляет класс в виде строки
        return f"x0={self.x0}, y0={self.y0}, x1={self.x1}, y1={self.y1}"

    def __repr__(self):  # Представляет класс в виде строки в объектах
        return f"(({self.x0}; {self.y0}), ({self.x1}; {self.y1}))"

    def __add__(self, other):
        return Bbox(min(self.x0, other.x0),
                    min(self.y0, other.y0),
                    max(self.x1, other.x1),
                    max(self.y1, other.y1))

    def _get_w_h(self):  # внутренний метод. Не для пользователя
        self.w = self.x1 - self.x0
        self.h = self.y1 - self.y0

    def get_area(self):
        return self.w * self.h


import os


class PathInfo:
    def __init__(self, path):
        self.path = path
        self._files = []
        self._folders = []
        self._get_list_dir()

    def _get_list_dir(self):
        path_list_dir = os.listdir(self.path)
        for item in path_list_dir:
            path_item = os.path.join(self.path, item)
            if os.path.isfile(path_item):
                self._files.append(item)
            else:
                self._folders.append(item)

    def __repr__(self):
        return f"Files: {self._files}\nFolders: {self._folders}"

    def show_files(self):
        return self._files

    def show_folders(self):
        return self._folders
