import sys
import os

from noaa_sdk import noaa
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

class Noaa_weather(NeuronModule):
    def __init__(self, **kwargs):
        # get message to spell out loud
        super(Noaa_weather, self).__init__(**kwargs)

        self.city= kwargs.get('city', None)
        self.state = kwargs.get('state', None)
        self.days = kwargs.get('days', 1)
        
        if not self._is_parameters_ok():
            raise InvalidParameterException
                
        n = noaa.NOAA()
        res = n.get_city_forecasts('Cleveland', 'Ohio', False)
        forecast = ''
        #day and night for each day 1-5 days
        for i in range(2*self.days):
            day = res[i]['name'] + ' , ' + res[i]["detailedForecast"]
            print(day)
            forecast = forecast + day + ' '
        self.say(forecast)


    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: NotImplementedError
        """
        if self.city is None:
            raise MissingParameterException("NWS neuron needs an city")
        if self.state is None:
            raise MissingParameterException("NWS neuron needs a state")
        if self.days < 1 or self.days > 5:
            raise MissingParameterException("NWS neuron needs days between 1 and 5")
 
        return True
