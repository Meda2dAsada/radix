from rich.syntax import Syntax
from textual.widgets import Static
from textual.app import ComposeResult
from textual.containers import ScrollableContainer

from src.classes.file import File


class CodeDisplay(ScrollableContainer):
    def __init__(self, file: File, language: str, theme: str = "material"):
        super().__init__()
        self.__code: Syntax = Syntax(file.content.strip(), language, theme=theme, line_numbers=True, indent_guides=True)
        self.__static = Static(self.__code)
        self.__static.styles.width = "auto"

        self.styles.height = 20
        self.styles.width = 80

    def compose(self) -> ComposeResult:
        yield self.__static
