"""
A demo shows the basic layout of a Kivy GUI.
This GUI will interact with user.
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo class"""
    def build(self):
        """Set the frame name and declare the .kv file path"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Output a string when click button 'Greet' """
        print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Clear two fields after clicked 'Clear' """
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


# Start running
BoxLayoutDemo().run()
