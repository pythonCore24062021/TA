class BasePage:
    def __init__(self, base_url: str):
        self.relative_path = None
        self.base_url = base_url

    def get_url(self):
        return self.base_url + self.relative_path
