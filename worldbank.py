'''Python library to access World Bank's open data

The official World Bank API documentation can be found at 
http://data.worldbank.org/developers .
'''

import urllib

try:
    import json
except ImportError:
    import simplejson as json
    
def _fetch(url):
    '''Downloads data from a JSON page and parses into python objects
    
    This method will work for any JSON encoded page, not just World Bank's data.
    '''
    
    f = urllib.urlopen(url)
    response = json.loads(f.read())
    f.close()
    return response
        
class WorldBank(object):
    '''WorldBank instances represent a connection (with minimal preferences)
    to the World Bank database.
    '''
    
    URL = 'http://api.worldbank.org/'
    
    def __init__(self, lang = 'en', per_page = 50):
        self.lang = lang
        self.per_page = per_page
        
    def get_all_pages(self, path, **kwargs):
        '''Fetches all of the pages for a given path sequentially.'''
        
        kwargs['page'] = 1
        first_page = self.request(path, **kwargs)
        data = first_page[1]
        for page in xrange(2, first_page[0]['pages'] + 1):
            kwargs['page'] = page
            data.extend(self.request(path, **kwargs)[1])
        return data
    
    def get_country(self, code='all', indicator='', **kwargs):
        '''Retrieves country data
        
        The code parameter should be the 2 letter ISO code for the country of
        interest. If no code is specified, data will be fetched for all 
        countries (this is the default behavior of the actual World Bank API).
        Regional or financial aggregate data can be collected by using the
        codes described at http://data.worldbank.org/node/246 . 
        
        The indicator is the string code for the indicator (statistic) of
        interest. See http://data.worldbank.org/node/203 for more info about
        indicators.
        '''
        
        if not indicator:
            return self.request('countries/' + code, **kwargs) 
        return self.request('countries/' + code + '/indicators/' + indicator,
                            **kwargs)
    
    def get_indicators(self, code='', **kwargs):
        '''More details at http://data.worldbank.org/node/203'''
        
        return self.request('indicators/' + code, **kwargs)
    
    def get_sources(self, **kwargs):
        '''More details at http://data.worldbank.org/node/210'''
        
        return self.request('sources', **kwargs)
        
    def get_topics(self, id='', **kwargs):
        '''Retrieve info on a topic or all of the topics
        
        If the id parameter is left as '', data on all the topics is fetched.
        If an numerical id is passed, data on that topic will be fetched.
        More details at http://data.worldbank.org/node/209'''
        
        return self.request('topics/' + str(id), **kwargs)
    
    def request(self, path, **kwargs):
        '''Utility function that concatenates the URL and calls _fetch'''
        
        kwargs['format'] = 'json'
        if not kwargs.get('per_page', False):
            kwargs['per_page'] = self.per_page
        return _fetch(self.URL + self.lang + '/' + path + '?' + 
                      urllib.urlencode(kwargs))