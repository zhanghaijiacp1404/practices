from kivy.app import App
from kivy.lang import Builder


DISTANCE_COEFFICIENT = 1.60934 # 1mile = 1.60934km


class ConvertMilesKm(App):
    def build(self):
        self.title = "convert miles to km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        miles_to_km = DISTANCE_COEFFICIENT * self.get_validated_miles()
        self.root.ids.output_label.text = str(miles_to_km)

    def handle_increment(self, value):
        self.root.ids.input_number.text = str(self.get_validated_miles() + value)
        self.handle_convert()

    def get_validated_miles(self):
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0


ConvertMilesKm().run()