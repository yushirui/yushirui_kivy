from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer


class VideoPlayerTest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        player = VideoPlayer(source='demo0.mp4', state='play',
                             options={'allow_stretch': True, 'eos': 'loop'})
        self.add_widget(player)


class VideoPlayerApp(App):
    def build(self):
        return VideoPlayerTest()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    VideoPlayerApp().run()