from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video


class VideoWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def on_position_change(instance, value):
            print('The position in the video is', value)

        def on_duration_change(instance, value):
            print('The duration of the video is', value)

        video = Video(source='34.mp4', state='play')
        video.bind(position=on_position_change, duration=on_duration_change)
        self.add_widget(video)


class VideoApp(App):
    def build(self):
        return VideoWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    VideoApp().run()
