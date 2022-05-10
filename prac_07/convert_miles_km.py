"""
A Kivy GUI application to convert miles to kilometers
"""

from kivy.app import App, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

# 1 mile = 1.60934 kilometer
DISTANCE_COEFFICIENT = 1.60934


class ConvertMilesKm(App):
    """ConvertMileKm class"""
    message = StringProperty()

    def build(self):
        """Build the kivy application based on existing .kv file"""
        Window.size = (800, 300)
        self.title = "convert miles to km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert miles to km, output the result"""
        miles_to_km = DISTANCE_COEFFICIENT * self.get_validated_miles()
        self.message = str(f"{miles_to_km:,.3f}")

    def handle_increment(self, value):
        """handle increment function"""
        self.root.ids.input_number.text = str(self.get_validated_miles() + value)
        self.handle_convert()

    def get_validated_miles(self):
        """If the user input is a calculable value, return it, otherwise return 0"""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0


# Start Application
ConvertMilesKm().run()
