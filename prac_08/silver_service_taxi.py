from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self,fanciness,**kwargs):
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        super().__init__(**kwargs)

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return super().__str__() + f" plus flagfall of ${self.flagfall}"