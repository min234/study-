import re 
p = re.compile("ca.e") 
# .(ca.e):은 문자의미 | care,cafe (o) | caffe(x)
# ^(^de): 문자열의 시작 | desk,destination (0)|fade(x)
# $ (se $) : 문자열의 끝 > case , base (o) | face (x)

def print_match(m):
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print("m.string:",m.string) # 입력받은 문자열 
        print("m.start():", m.start ) # 일치하는 문자열의 시작 index
        print("m.end():",m.end()) # 일치하는 문자열의 끝 index
        print("m.span():",m.span()) # 일치하는 문자열의 시작 / 끝 index 
    else:
        print('매치가 안됨')

# m = p.match("cade")
# print_match(m)

# match 처음부터 일치하는거 확인
# search 주어진 문자열 중 일치 하는거

# m = p.search("careless") 
# print_match(m)

lst = p.findall("care cafe cabe") # 일치하는 모든걸 리스트 형태로 
print(lst)

 