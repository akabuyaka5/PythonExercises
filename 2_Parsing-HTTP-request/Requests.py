import json
import re
# El string que vamos a utilizar es
get = "GET /echo?message=%22Hello%20World!%22 HTTP/1.1\r\nHost: 127.0.0.1:5005\r\nConnection:keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36\r\nSec-Fetch-Dest:document\r\nAccept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8, application/signedexchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User:?1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: es-ES,es;q=0.9, en-GB;q=0.8,en;q=0.7\r\n\r\n"
post = "POST /echo HTTP/1.1\r\nHOST: 127.0.0.1:5005\r\ncontent-type:application/x-www-form-urlencoded\r\ncontent-length: 23\r\n\r\nmessage=Hello World!!!!"
miDiccionario = dict()
strip = re.sub('[\r]', '', get)
strip = re.split('[\n]', strip)
strip = list(filter(''.__ne__, strip))

for line in strip:

    if line.__contains__('GET'):
        pal = line.split(' ')
        miDiccionario['Method'] = pal[0]
        miDiccionario['URL'] = pal[1]
        miDiccionario['Version'] = pal[2]
        val = pal[1].split('=', 1)
        listMessage = {'message': val[1]}
    elif line.__contains__('POST'):
        pal = line.split(' ')
        miDiccionario['Method'] = pal[0]
        miDiccionario['URL'] = pal[1]
        miDiccionario['Version'] = pal[2]
    elif line.__contains__('HTTP'):
        val = line.split('/', 1)
        miDiccionario[val[0].strip()] = val[1].strip()
    elif line.__contains__('message'):
        val = line.split('=', 1)
        listMessage = {val[0]: val[1]}
        miDiccionario['Params'] = listMessage
    else:
        val = line.split(':', 1)
        miDiccionario[val[0].strip()] = val[1].strip()

miDiccionario['Params'] = listMessage

print(json.dumps(miDiccionario, indent=2))
