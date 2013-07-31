import urllib
from xml.dom import minidom

def search(term, search_type):
        app_id="8B11A868EB6D329E446714969BFE784E1A0175BF"
        search_url = "http://api.search.live.net/xml.aspx?Appid=%s&query=%s&sources=%s" % (app_id, term, search_type)
        return minidom.parse(urllib.urlopen(search_url))

def parse_results(results_object):
        res = []
        for node in results_object.getElementsByTagName("news:NewsResult"):
                title = node.getElementsByTagName("news:Title")[0].childNodes
                url = node.getElementsByTagName("news:Url")[0].childNodes
                abstract = node.getElementsByTagName("news:Snippet")[0].childNodes
                date = node.getElementsByTagName("news:Date")[0].childNodes
                for t in title:
                        for u in url:
                                for a in abstract:
                                        for d in date:
                                                res.append([t.data, u.data, a.data, d.data])
        return res


