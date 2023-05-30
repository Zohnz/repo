import re

str1 = '1X, TEXT ABC 123 A1B2C3'
reg1 = r'\D(\d)'
print(re.findall(reg1, str1))


str2 = 'text from #START# till #END#'
reg2 = r'(?<=#START#).*?(?=#END#)'
print(re.findall(reg2, str2))


str3 = '12_34__56'
reg3 = r'(\d+)_[^_]'
print(re.findall(reg3, str3))