import requests, bs4, wikipedia

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
        print(e.message)

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
        print(e.message)
