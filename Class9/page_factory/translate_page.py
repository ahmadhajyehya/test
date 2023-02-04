from seleniumpagefactory.Pagefactory import PageFactory


class TranslatePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'text_box': ('CLASS_NAME', "er8xn")
    }

    def set_translate_text(self):
        self.text_box.set_text('hello')
