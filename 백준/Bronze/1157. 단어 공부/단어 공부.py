text = input().upper()
text_list = list(set(text))

count = {}

for i in range(len(text_list)):
    count[text_list[i]] = text.count(text_list[i])

result = [k for k, v in count.items() if max(count.values()) == v]

if len(result) == 1:
    print(result[0])  # 최빈 문자가 하나일 경우, 그 문자 출력
else:
    print("?")