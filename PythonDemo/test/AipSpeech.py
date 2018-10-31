
#-*-coding:utf-8 -*-
#!/usr/bin/python

from aip import AipSpeech
import playsound

APP_ID = '14382120'
API_KEY = 'lyGprYrD2KQqyRvdonuFKQya'
SECRET_KEY = 'hlrGloULpB2N1VZmTPBVcrLc6Iag0SEd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('今天天气不错', 'zh', 1, {
    'vol': 5,
})

if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

playsound.playsound('auido.mp3', True)

