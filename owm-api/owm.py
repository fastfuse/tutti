import requests
import os

API_KEY = os.environ.get("API_KEY", "cb886c132408a168ef9af698238e122a")


# class OpenWeatherMap:
#     """
#     Main OpenWeatherMap API handler
#     """
#
#     BASE_URI = "https://api.openweathermap.org/data/2.5"
#     WEATHER_URI = f"{BASE_URI}/weather"
#     FORECAST_URI = f"{BASE_URI}/forecast"
#
#     def __init__(self, api_key, **kwargs):
#         self._api_key = api_key
#         self._session = requests.Session()
#
#     def weather(self, city="", city_id=None, units="metric"):
#         """
#         Method to get current weather data.
#
#         :param city:
#         :param city_id:
#         :param units:
#         :return:
#         """
#
#         payload = {
#             "appid": self._api_key,
#             "units": units
#         }
#
#         if city:
#             payload.update({"q": city})
#
#         elif city_id:
#             payload.update({"id": city_id})
#
#         resp = self._session.get(self.WEATHER_URI, params=payload)
#
#         return resp.json()
#
#     def forecast(self, city="", city_id=None, units="metric"):
#         """
#         Method to get forecast for 5 days / 3 hours
#         :param city:
#         :param city_id:
#         :param units:
#         :return:
#         """
#         payload = {
#             "appid": self._api_key,
#             "units": units
#         }
#
#         if city:
#             payload.update({"q": city})
#
#         elif city_id:
#             payload.update({"id": city_id})
#
#         resp = self._session.get(self.FORECAST_URI, params=payload)
#
#         return resp.json()


class OpenWeatherMap:
    """
    Main OpenWeatherMap API handler
    """

    BASE_URI = "https://api.openweathermap.org/data/2.5"
    WEATHER_URI = f"{BASE_URI}/weather"
    FORECAST_URI = f"{BASE_URI}/forecast"

    def __init__(self, api_key, city, units="metric"):
        self._api_key = api_key
        self._session = requests.Session()
        self._city = city
        self._units = units

        self._payload = self._compose_payload()

    def _compose_payload(self):
        payload = {
            "appid": self._api_key,
            "units": self._units
        }

        if isinstance(self._city, int):
            payload.update(id=self._city)
        else:
            payload.update(q=self._city)

        return payload

    def current_weather(self):
        """
        Method to get current weather data
        """

        resp = self._session.get(self.WEATHER_URI, params=self._payload)

        return resp.json()

    def forecast(self):
        """
        Method to get forecast for 5 days / 3 hours
        """

        resp = self._session.get(self.FORECAST_URI, params=self._payload)

        return resp.json()
