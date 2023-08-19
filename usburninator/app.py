from textual.app import App, ComposeResult
from textual.widgets import Placeholder


class USBurninator(App):
    """Main wrapper"""

    def compose(self) -> ComposeResult:
        yield Placeholder("Hello", variant="text", id="hello")


def start():
    """main function"""
    USBurninator().run()


if __name__ == "__main__":
    start()
