from falsy.falsy import FALSY

f = FALSY()
f.swagger('spec1.yml', ui=True, ui_language='en', theme='normal')
api = f.api
