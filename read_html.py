__author__ = 'Maxwell'
#- coding: utf-8
import cookielib
import urllib
import urllib2
PROXY =['50.31.106.161:8800',
        '50.31.106.47:8800']
AGENT = ['Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
         'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
         'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
         'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2',
         'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.16) Gecko/20120427 Firefox/15.0a1',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0a2) Gecko/20111101 Firefox/9.0a2',
         'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
         'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
         ]

class Get_Url():
    def __init__(self, proxy=None):
        if not proxy:
            import random
            proxy = random.sample(PROXY,1)[0]

        cj = cookielib.LWPCookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cj)
        if proxy:
            proxy_handler = urllib2.ProxyHandler({'http': proxy})
            opener = urllib2.build_opener(proxy_handler, cookie_handler)
        else:
            opener = urllib2.build_opener(cookie_handler)
        urllib2.install_opener(opener)


    def _url_open(self, url, data=None, headers=None):
        import random
        if not headers:
            headers = {}

        headers['User-agent'] = random.sample(AGENT,1)
        headers['Accept'] = 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'
        headers['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
        headers['Connection'] = 'keep-alive'

        encoded_data = urllib.urlencode(data) if data else None

        req = urllib2.Request(url, encoded_data, headers)

        handle = urllib2.urlopen(req)

        return handle


    def read(self, url, parametros=None):
        """Retorna o detalhe da Pagina"""
        handle = self._url_open(url, parametros)
        html = handle.read()
        return html
