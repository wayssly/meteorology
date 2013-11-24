import json
import urllib.request

class weather:
    def __init__(self, version, mode, lang, units):
        # Setting API's version.
        # Latest version: 2.5.
        self.version = version

        # Setting API's answer mode.
        # Supported modes: json or xml.
        self.mode = mode

        # Settings API's answer language.
        # Supported languages: English - en, Russian - ru, Italian - it, Spanish - sp,
        #                      Ukrainian - ua, German - de, Portuguese - pt, Romanian - ro,
        #                      Polish - pl, Finnish - fi, Dutch - nl, French - fr,
        #                      Bulgarian - bg, Swedish - se, Chinese Traditional - zh_tw,
        #                      Chinese Simplified - zh_cn, Turkish - tr.
        self.lang = lang

        # You can use different types of metric systems by units.
        # Supported metric systems: metric or imperial.
        self.units = units

        # Generation request URI using received arguments.
        self.request_uri = 'http://api.openweathermap.org/data/%s/weather?mode=%s&lang=%s&units=%s' % (self.version, self.mode, self.lang, self.units)

    def by_city(self, q):
				# Current weather.
        # RSVPs using city name, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&q=%s' % (self.request_uri, q)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_coordinats(self, lat, lon):
				# Current weather.
        # RSVPs using geographic coordinats, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&lon=%s&lat=%s' % (self.request_uri, lon, lat)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_identifier(self, id):
				# Current weather.
        # RSVPs using city ID, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&id=%s' % (self.request_uri, id)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def trash(self):
        # Removing unneeded variables.
        del(self.value)
        del(self.page)
        
class forecast:
    def __init__(self, version, mode, lang, units):
        # Setting API's version.
        # Latest version: 2.5.
        self.version = version

        # Setting API's answer mode.
        # Supported modes: json or xml.
        self.mode = mode

        # Settings API's answer language.
        # Supported languages: English - en, Russian - ru, Italian - it, Spanish - sp,
        #                      Ukrainian - ua, German - de, Portuguese - pt, Romanian - ro,
        #                      Polish - pl, Finnish - fi, Dutch - nl, French - fr,
        #                      Bulgarian - bg, Swedish - se, Chinese Traditional - zh_tw,
        #                      Chinese Simplified - zh_cn, Turkish - tr.
        self.lang = lang

        # You can use different types of metric systems by units.
        # Supported metric systems: metric or imperial.
        self.units = units

        # Generation request URI using received arguments.
        self.request_uri = 'http://api.openweathermap.org/data/%s/forecast?mode=%s&lang=%s&units=%s' % (self.version, self.mode, self.lang, self.units)
        self.request_uri_daily = 'http://api.openweathermap.org/data/%s/forecast/daily?mode=%s&lang=%s&units=%s' % (self.version, self.mode, self.lang, self.units)

    def by_city(self, q):
				# Forecast every 3 hours.
        # RSVPs using city name, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&q=%s' % (self.request_uri, q)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_coordinats(self, lat, lon):
				# Forecast every 3 hours.
        # RSVPs using geographic coordinats, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&lon=%s&lat=%s' % (self.request_uri, lon, lat)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_identifier(self, id):
				# Forecast every 3 hours.
        # RSVPs using city ID, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&id=%s' % (self.request_uri, id)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_city_daily(self, q, cnt):
				# Daily forecast (maximum 14 days).
        # RSVPs using city name, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&q=%s&cnt=%s' % (self.request_uri_daily, q, cnt)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_coordinats_daily(self, lat, lon, cnt):
				# Daily forecast (maximum 14 days).
        # RSVPs using geographic coordinats, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&lon=%s&lat=%s&cnt=%s' % (self.request_uri_daily, lon, lat, cnt)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_identifier_daily(self, id, cnt):
				# Daily forecast (maximum 14 days).
        # RSVPs using city ID, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&id=%s&cnt=%s' % (self.request_uri_daily, id, cnt)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def trash(self):
        # Removing unneeded variables.
        del(self.value)
        del(self.page)

class find:
    def __init__(self, version, mode, lang, units):
        # Setting API's version.
        # Latest version: 2.5.
        self.version = version

        # Setting API's answer mode.
        # Supported modes: json or xml.
        self.mode = mode

        # Settings API's answer language.
        # Supported languages: English - en, Russian - ru, Italian - it, Spanish - sp,
        #                      Ukrainian - ua, German - de, Portuguese - pt, Romanian - ro,
        #                      Polish - pl, Finnish - fi, Dutch - nl, French - fr,
        #                      Bulgarian - bg, Swedish - se, Chinese Traditional - zh_tw,
        #                      Chinese Simplified - zh_cn, Turkish - tr.
        self.lang = lang

        # You can use different types of metric systems by units.
        # Supported metric systems: metric or imperial.
        self.units = units

        # Generation request URI using received arguments.
        self.request_uri = 'http://api.openweathermap.org/data/%s/find?mode=%s&lang=%s&units=%s' % (self.version, self.mode, self.lang, self.units)

    def by_city(self, q):
				# Find location.
        # RSVPs using city name, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&q=%s' % (self.request_uri, q)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def by_coordinats(self, lat, lon):
				# Find location.
        # RSVPs using geographic coordinats, then return the JSON-array.
        self.page = urllib.request.urlopen('%s&lon=%s&lat=%s' % (self.request_uri, lon, lat)).read().decode('utf-8')
        if self.mode == 'json': self.value = json.loads(self.page)
        elif self.mode == 'xml': self.value = self.page
        return self.value

    def trash(self):
        # Removing unneeded variables.
        del(self.value)
        del(self.page)
