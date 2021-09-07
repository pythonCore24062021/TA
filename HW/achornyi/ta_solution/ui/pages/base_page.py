from ui.components.base_page.header import Header


class BasePage:
    def __init__(self, relative_path: str):
        self.relative_path = relative_path
        self.header = Header()

