import urllib
import simplejson
import requests

def search(term, search_type):
	quote = urllib.quote("\'"+term+"\'")
        app_id="64Wn5jmFDbj7CEcr5VG5MaLqnz3FnDOSIeXyxIADzTA="
        r = requests.get("https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/%s?Query=%s&$format=json" % (search_type,quote), auth=(app_id, app_id))
        print "done search"
	l = simplejson.loads(r.content)
	return l

def parse_results(results_object):
        res = []
        for node in results_object[u'd'][u'results']:
                title = node[u'Title']
                url = node[u'Url']
                abstract = node[u'Description']
                date = node[u'Date']
                res.append([title, url, abstract, date])
        return res

