import json
import re

def requests(request):
    dictionary = dict()
    strip = re.sub('[\r]', '', request)
    strip = re.split('[\n]', strip)
    strip = list(filter(''.__ne__, strip))
    text = False
    for line in strip:

        if line.__contains__('GET'):
            pal = line.split(' ')
            dictionary['Method'] = pal[0]
            dictionary['URL'] = pal[1]
            dictionary['Version'] = pal[2]
            if (line.__contains__('message')):
                val = pal[1].split('=', 1)
                list_message = {'message': val[1]}
                text = True

        elif line.__contains__('POST'):
            pal = line.split(' ')
            dictionary['Method'] = pal[0]
            dictionary['URL'] = pal[1]
            dictionary['Version'] = pal[2]

        elif line.__contains__('HTTP'):
            val = line.split('/', 1)
            dictionary[val[0].strip()] = val[1].strip()

        elif line.__contains__('message'):
            val = line.split('=', 1)
            list_message = {val[0]: val[1]}
            dictionary['Params'] = list_message
        elif line.__contains__('fname'):
            name = line.split('&', 1)
            dictionary['Params'] = {}
            for i in range(len(name)):
                val = name[i].split('=', 1)
                dictionary['Params'].update({val[0]: val[1]})

            # dictionary['Params'] = list_message
        else:
            val = line.split(':', 1)
            dictionary[val[0].strip()] = val[1].strip()
    if (text):
        dictionary['Params'] = list_message

    print("Parser function:")
    print(json.dumps(dictionary, indent=2))
    return dictionary
