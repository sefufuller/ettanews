import urllib
import simplejson
import requests
import kaleb

def search(term, search_type):
	quote = urllib.quote("\'"+term+"\'")
        app_id="1p359jn78P6GP1b1TKw+EvXYwIjPjuly+RbAaga7Jlg="
        r = requests.get("https://api.datamarket.azure.com/Data.ashx/Bing/Search/%s?$format=json&Query=%s" % (search_type,quote), auth=(app_id, app_id))
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
		kaleb.Post(title+"\n"+url+"\n"+abstract)
                res.append([title, url, abstract, date])
        return res

