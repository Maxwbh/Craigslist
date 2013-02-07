import urllib2

urlfile = urllib2.urlopen("http://www.msbrasil.inf.br/clientes")

data_list = []
chunk = 4096
while 1:
    data = urlfile.read(chunk)
    if not data:
        print "done."
        break
    data_list.append(data)
    print "Read %s bytes"%len(data)