import urllib.request
import json
import datetime

class UrlGrabber(object):
	#constructor
	#dataDepth is the number of days the UrlGrabber will pull
	def __init__(self, dataDepth=10):
		response = urllib.request.urlopen("http://api.fixer.io/latest")
		encoding = response.info().get_content_charset('utf8')
		result = json.loads(response.read().decode(encoding))
		
		self.samples = dataDepth
		self.base = result["base"]
		self.data = {self.base : [1]}
		
		for i,j in result["rates"].items():
			self.data[i] = []
			self.data[i].append(j)
		
		offset = datetime.timedelta(days=1)
		date = datetime.date.today() - offset
		for i in range(dataDepth-1):
			response = urllib.request.urlopen("http://api.fixer.io/" + str(date))
			encoding = response.info().get_content_charset('utf8')
			result = json.loads(response.read().decode(encoding))
			
			self.data[self.base].append(1)
			for j,k in result["rates"].items():
				self.data[j].insert(0, k)
			date -= offset
	
	#return a list of the currency codes
	def getCurrencies(self):
		abv = []
		abv.append(self.base)
		for i,j in self.data.items():
			abv.append(i)
		return abv
	
	#return time series data for a particular currency
	def getTimeSeriesData(self, currency):
		return self.data[currency]
	
	#return current currency value
	def getCurrentValue(self, currency):
		return self.data[currency][self.samples - 1]
	
	#return trend for a particular currency
	#in the range of -2, -1, 0, 1, 2
	def getCurrencyTrend(self, currency):
		#from http://mathworld.wolfram.com/LeastSquaresFitting.html
		def slopeOnRange(low, high):
			xy = 0
			xx = 0
			
			mx = 0
			my = 0
			
			n = high - low + 1
			
			for i in range(low, high+1):
				mx += i
				my += self.data[currency][i]
			
			mx /= n
			my /= n
			for i in range(low, high+1):
				t = i - mx
				xy += ( t * (self.data[currency][i] - my) )
				xx += ( t * t )
			
			return xy / xx
		s1 = slopeOnRange(0, int((self.samples-1) / 2))
		s2 = slopeOnRange(int((self.samples-1) / 2) + 1, self.samples-1)
		
		#step discovered empirically
		step = .002
		
		if s2 > s1 + 3 * step :
			return 2
		if s2 > s1 + step :
			return 1
		if s2 > s1 - step :
			return 0
		if s2 > s1 - 3 * step :
			return -1
		return -2
#end of UrlGrabber
