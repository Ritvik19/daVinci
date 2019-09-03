import requests, bs4
import wikipedia, hastebin
import re

def haste(arg):
    try:
        return hastebin.post(arg)
    except  Exception as e:
        print(e)

def wiki(arg):
    try:
        search_results = wikipedia.search(arg)
        if search_results != []:
            reply = wikipedia.summary(search_results[0], 5)
            reply += '\n\nRead More: ' + wikipedia.page(search_results[0]).url
            return reply
        else:
            return 'No results Found'
    except Exception as e:
        print(e)

def cambridge(arg):
    url = 'https://dictionary.cambridge.org/dictionary/english/'+arg.lower()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == requests.codes.ok:
            ressoup = bs4.BeautifulSoup(res.text, 'lxml')
            pos = ressoup.select('div.pos-header')[0].select('span.pos')
            pos_ = []
            for e in pos:
                pos_.append(e.getText().strip())
            definition = ressoup.select('div.entry-body__el')[0].select('p.def-head.semi-flush')
            example = ressoup.select('div.entry-body__el')[0].select('span.eg')
            result = ressoup.select('div.entry-body__el')[0].select('span.hw')[0].getText().strip()
            result += '\n' + ', '.join(pos_) + '\n\n'
            for e1, e2 in zip(definition, example):
                result += e1.getText()+'\n'+e2.getText()+'\n\n'
            result += 'Read More: '+url

            return result
        else:
            print('Something went wrong')
    except Exception as e:
        print(e)
        return 'No meanings found'

def woof():
    try:
        allowed_extension = ['jpg','jpeg','png']
        file_extension = ''
        while file_extension not in allowed_extension:
            url = requests.get('https://random.dog/woof.json').json()['url']
            file_extension = re.search("([^.]*)$",url).group(1).lower()
        return url
    except Exception as e:
        print(e)

def cricbuzz():
    url = 'https://www.cricbuzz.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == requests.codes.ok:
            ressoup = bs4.BeautifulSoup(res.text, 'lxml')
            elems = ressoup.select('div.cb-col.cb-col-25.cb-mtch-blk')
            output = []
            for e in elems:
                o = ""
                divs = e.select('div')
                if len(divs) == 3:
                    for ed in e.select('div')[:2]:
                        o += ed.getText() + "\n"
                elif len(divs) == 7:
                    o += divs[1].getText() + " "
                    o += divs[2].getText() + "\n"
                    o += divs[4].getText() + " "
                    o += divs[5].getText() + "\n"
                    o += divs[6].getText() + "\n"
                o += url+e.select('a')[0].get('href')
                output.append(o)
            output = '\n'.join(list(set(output)))
            return output
        else:
            print('Something went wrong')
    except Exception as e:
        print(e)
        return "Scores couldn't be fetched"

def stackoverflow(query):
    url_query = 'https://stackoverflow.com/search?q='+query
    try:
        res = requests.get(url_query)
        if res.status_code == requests.codes.ok:
            ressoup = bs4.BeautifulSoup(res.text, 'lxml')
            elems = ressoup.select('.question-summary')
            results = ""
            for i,e in enumerate(elems):
                l = 'https://stackoverflow.com'+re.findall(r'href="(.*?)"', str(list(e.children)[3]))[0]
                t = re.findall(r'<a .*? title="(.*?)">', str(list(e.children)[3]))[0]
                results += str(i+1)+'\n'+t+'\n'+l+'\n\n'
        return results
    except Exception as e:
        print(e)
        return "Scores couldn't be fetched"
