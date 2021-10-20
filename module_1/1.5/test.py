s = "HackerRank.com PreSenTs \"Pythonist 2"
res = ''
for i in s:
    if i.isupper():
        res += i.lower()
    else:
        res += i.upper()

# print(res)


for idx, subs in enumerate(s):
    slu = subs.lower() if subs.isupper() else subs.upper()
    s = slu + s[1:] if idx == 0 else s[:idx] + slu + s[idx+1:]

print('result:  ', s)
