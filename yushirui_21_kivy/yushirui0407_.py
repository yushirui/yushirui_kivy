from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ImageBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ImageApp(App):
    def build(self):
        return ImageBoxLayout()


if __name__ == '__main__':
    ImageApp().run()
