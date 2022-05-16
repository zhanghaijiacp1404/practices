"""SilverServiceTaxi class"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Representing a SilverServiceTaxi object"""
    flagfall = 4.5

    def __init__(self, fanciness, **kwargs):
        """Initialize a SilverServiceTaxi instance"""
        super().__init__(**kwargs)
        # Multiply the fanciness variable to price_per_km variable
        self.price_per_km *= fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """return the fare for silver service taxi"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi object"""
        return super().__str__() + f" plus flagfall of ${self.flagfall}"
