from src.classes.entry import Entry
from src.constants.const import FILE
from src.classes.entry_creator import EntryCreator

class File(Entry):
    def __init__(self, name: str, path: str = None, content: str | None = None):
        super().__init__(name, path, FILE)
        self.__content: str = None
        self.content: str = content

    @property
    def split_name(self) -> tuple[str, str]:
        return File.trim(self)
    
    @property
    def file_name(self) -> str:
        return self.split_name[0]
    
    @property
    def extension(self) -> str:
        return self.split_name[1]

    @property
    def content(self) -> str:
        return self.__content
    
    @content.setter
    def content(self, content: str) -> None:
        self.__content = content if self.not_empty(content) else ''

    @property
    def is_empty(self) -> bool:
        return not bool(self.__content)

    def write_self(self):
        EntryCreator.write_file(self.absolute_path, self.content)

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other: 'File'):
        if not isinstance(other, File):
            return False
        return super().__eq__(other) and self.content == other.content
    
    @staticmethod
    def format_split_name(file: 'File', sizes: tuple[int]) -> str | None:
        if len(sizes) == 2 and all(isinstance(size, int) for size in sizes):
            return [f'[{file[:size]}\u2026]' if len(file) > size else file for file, size, in zip(file.split_name, sizes)]

    @staticmethod
    def trim(file: 'File') -> tuple[str, str] | None:

        if isinstance(file, File):
            if '.' not in file.name:
                return file.name, ''

            split = file.name.split('.')
            extension = split.pop()
            
            return '.'.join(split), extension

    @staticmethod
    def join(file: 'File') -> str | None:
        if isinstance(file, File):
            start, end = file.split_name
            if end:
                return '.'.join(file.split_name)

            return ''.join(start)
