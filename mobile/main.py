from kivy.app import App
from kivy.uix.label import Label


class PocketCloudApp(App):
    def build(self):
        return Label(text="PocketCloud - Hello World")


PocketCloudApp().run()