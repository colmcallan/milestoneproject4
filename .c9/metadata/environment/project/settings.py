{"filter":false,"title":"settings.py","tooltip":"/project/settings.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":90,"column":0},"end":{"row":101,"column":0},"action":"remove","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }","",""],"id":94},{"start":{"row":90,"column":0},"end":{"row":101,"column":1},"action":"insert","lines":["if 'DATABASE_URL' in os.environ:","    DATABASES = {","        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","        }","else:","    print('no db found')","    DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}"]}]]},"ace":{"folds":[],"scrolltop":1032.5,"scrollleft":0,"selection":{"start":{"row":101,"column":1},"end":{"row":101,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":70,"state":"start","mode":"ace/mode/python"}},"timestamp":1567028627620,"hash":"0f9264b90205871ceaca56c33377a86fb91bba95"}