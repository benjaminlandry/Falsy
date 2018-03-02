from falsy.falsy import FALSY

f = FALSY()
f.swagger('spec1.yml', ui=True, ui_language='en', theme='normal')
# f.swagger('spec2.yml', ui=True, ui_language='zh-cn', theme='normal')
api = f.api
