
from HW.rrasi.HW6.Register.pages.register_page import RegisterUser



class Message(RegisterUser):
    def get_message(self):
        return self.element.text