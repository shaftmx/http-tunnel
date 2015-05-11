import urllib2

def get_proxy_opener(proxyurl, proxyuser, proxypass, proxyscheme="http"):
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, proxyurl, proxyuser, proxypass)

    proxy_handler = urllib2.ProxyHandler({proxyscheme: proxyurl})
    proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)

    return urllib2.build_opener(proxy_handler, proxy_auth_handler)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 4:
        url_opener = get_proxy_opener(*sys.argv[1:4])
        for url in sys.argv[4:]:
            print url_opener.open(url).headers
    else:
        print "Usage:", sys.argv[0], "proxy user pass fetchurls..."



#import urllib2
#
#proxy = urllib2.ProxyHandler({'http': 'http://
#username:password@proxyurl:proxyport'})
#auth = urllib2.HTTPBasicAuthHandler()
#opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
#urllib2.install_opener(opener)
#
#conn = urllib2.urlopen('http://python.org')
#return_str = conn.read()
