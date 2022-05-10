"""
Dynamic Widgets / Labels program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelApp class"""
    def __init__(self, **kwargs):
        """Start to initialize the app"""
        super().__init__(**kwargs)
        # Suppose we have a name list like this:
        self.names = ["Jack", "Annie", "Bob", "Ken"]

    def build(self):
        """Build the GUI app based on .kv file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Start creating dynamic labels"""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))


# Start running
DynamicLabelsApp().run()