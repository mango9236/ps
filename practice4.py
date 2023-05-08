from collections import defaultdict
import random

# list가 default값인 딕셔너리 생성
prefix_dict = defaultdict(list) 

# txt.file 읽기
FakeText = "" # 가짜 텍스트
f = open('HarryPotter.txt', 'r')
txt = f.read().split() # 단어마다 읽어옴
f.close()

# key_value쌍 
for i in range(2,len(txt)): 
    txt_tuple = (txt[i-2],txt[i-1]) # 텍스트 튜플
    if txt[i] not in prefix_dict[txt_tuple]: # key에 대응되는 value가 prefix_dict에 존재하지 않으면
        prefix_dict[txt_tuple].append(txt[i]) # 대응되는 value 추가


prefix = input() # 제시어 입력 
FakeText += prefix # 입력한 단어는 무조건 들어감
text = prefix.split() # 두 단어를 쪼갬
txt_tuple = (text[0], text[1]) # 검색할 튜플
cnt = 1 # 단어 카운트

# 단어 100개 이하, 그리고 단어 
while prefix_dict[txt_tuple] and cnt <= 100 and len(prefix_dict[txt_tuple]) >= 1:
    suffix = random.randint(0,len(prefix_dict[txt_tuple])-1) # prefix에 대응되는 value 랜덤으로 선정
    FakeText +=  " " + prefix_dict[txt_tuple][suffix] # 선택된 suffix를 추가
    txt_tuple = (txt_tuple[1], prefix_dict[txt_tuple][suffix]) # 뒷 단어 + suffix = 새로운 튜플
    cnt += 1 # 단어 카운트 증가

# 가짜 문장 출력
print(FakeText) 

