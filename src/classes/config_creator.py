from src.classes.file import File
from src.classes.directory import Directory
from src.classes.json_reader import JsonReader
from src.classes.path_manager import PathManager
from src.classes.entry_creator import EntryCreator

class ConfigCreator:
    RADIX_DIR: str = '.radix'
    JSON_DIR: str = 'json'
    STYLE_DIR: str = 'style'
    FILES_FILE: str = 'files.json'
    DIRECTORIES_FILE: str = 'directories.json'
    TEMPLATES_FILE: str = 'templates.json'
    RADIX_FILE: str = 'radix.json'
    STYLE_FILE: str = 'style.tcss'

    @staticmethod
    def working_dir(radix_path: bool):
        return PathManager.get_user_path() if not radix_path else PathManager.join(
            ConfigCreator.RADIX_DIR,
            PathManager.get_user_path()
        )

    @staticmethod
    def get_style_file():
        return PathManager.join(
            ConfigCreator.STYLE_FILE,
            ConfigCreator.working_dir(True),
            ConfigCreator.STYLE_DIR
        )

    @staticmethod
    def get_json_dir():
        return PathManager.join(
            ConfigCreator.JSON_DIR,
            ConfigCreator.working_dir(True)
        )
    
    @staticmethod
    def create_config():
        root_path = ConfigCreator.working_dir(False)
        # config files

        style_file = File(ConfigCreator.STYLE_FILE)
        files_file = File(ConfigCreator.FILES_FILE, content='{}')
        directories_file = File(ConfigCreator.DIRECTORIES_FILE, content='{}')
        templates_file = File(ConfigCreator.TEMPLATES_FILE, content='{}')
        radix_file = File(ConfigCreator.RADIX_FILE, content='{}')

        # radix styles folder
        styles_dir = Directory(ConfigCreator.STYLE_DIR)
        styles_dir.add(style_file)

        json_dir = Directory(ConfigCreator.JSON_DIR)
        json_dir.content = [files_file, directories_file, templates_file]

        # radix root folder
        radix_dir = Directory(ConfigCreator.RADIX_DIR, root_path)
        radix_dir.content = [styles_dir, json_dir]
        radix_dir.write_self()
        ConfigCreator.__re_write_config(radix_dir.content)
    
    @staticmethod
    def __re_write_config(directories: list[Directory]):
        for directory in directories:
            for entry in directory.content:
                path = entry.absolute_path

                if isinstance(entry, File):
                    if not JsonReader.is_valid_json(path, False) or entry.is_empty:
                        EntryCreator.delete_file(path)
                    entry.write_self()