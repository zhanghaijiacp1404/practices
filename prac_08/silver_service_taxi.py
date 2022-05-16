"""SilverServiceTaxi class"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Representing a SilverServiceTaxi object"""
    flagfall = 4.5

    def __init__(self,fanciness, **kwargs):
        """Initialize a SilverServiceTaxi instance"""
        super().__init__(**kwargs)
        self.price_per_km *= fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """Get current fare, overrides this method for parent class"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi instance"""
        return super().__str__() + f" plus flagfall of ${self.flagfall}"