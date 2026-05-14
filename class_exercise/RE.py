#設定一個字串 三種不重複RE 輸出
import re
s= "12 XY ABC XYZ12 56DEF B89CD CDE12"

#1. 12 XY
print(re.match(r'^.*?Y',s)[0])
#2. ABC XYZ12
print(re.findall(r'\D\D\D\W\D\D\D\d\d',s)[0])
#3. 56DEF B89CD CDE12
print(re.findall(r'[B-F1-9]{5}\s[B-F1-9]{5}\s[B-F1-9]{5}',s)[0])