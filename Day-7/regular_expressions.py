import re
# match = re.search(pat,text)

def Find(pat,text):
    match = re.search(pat,text)
    if match: print(match.group())
    else: print('not found')
Find('....g','piiiigs')