import wolframalpha
import webscraping
import random

appId = 'APER4E-58XJGHAVAK'
client = wolframalpha.Client(appId)

def removeBrackets(variable):
    return variable.split('(')[0]

def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']

def reply(text=''):
    if text.lower() in ["hi", "how are you", "is anyone there?", "hello", "good day", "hey"]:
        return random.choice(["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"])
    elif text.lower() in ["bye", "see you later", "goodbye"]:
        return random.choice(["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."])
    elif text.lower() in ["thanks", "thank you", "that's helpful", "that was helpful", "ohh that's great"]:
        return random.choice(["Happy to help!", "Any time!", "My pleasure"])
    else:
        res = client.query(text)
        if res['@success'] == 'false':
            return "Sorry I couldn't get this.\nTry /help for know more about how I can help you"
        else:
            result = ''
            pod0 = res['pod'][0]
            pod1 = res['pod'][1]
            if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                result = resolveListOrDict(pod1['subpod'])
                return result
            else:
                question = resolveListOrDict(pod0['subpod'])
                question = removeBrackets(question)
                return webscraping.wiki(question)
