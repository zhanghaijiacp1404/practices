from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self,fanciness, **kwargs):
        super().__init__(**kwargs)
        self.price_per_km *= fanciness
        self.fanciness = fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return super().__str__() + f" plus flagfall of ${self.flagfall}"