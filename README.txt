py-worldbank is a wrapper to the World Bank API.
The formal specification of the World Bank API can be found at http://data.worldbank.org/developers .

Example code:

from worldbank import WorldBank

wb = WorldBank()	#"lang" and "per_page" are allowed kwargs. 
Represents a connection to World Bank
brazil = wb.get_country(code='br')	#gets general data on brazil from world bank
brazil_gdp = wb.get_country(code='br', indicator='NY.GDP.MKTP.CD')	#GDP of Brazil in US dollars
indicators = wb.get_indicators()	#a list of all the indicators

The code is quite well documented and short, other available methods can be seen there.
