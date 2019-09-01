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
        return e.message
