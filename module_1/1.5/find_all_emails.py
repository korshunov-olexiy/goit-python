import re


def find_all_emails(text):
    result = re.findall(
        r"[A-Z|a-z][A-Z|a-z|\d._]{1,}@[A-Z|a-z]{1,}\.\w{2,}", text)
    return result


''' === RIGHT RESULT ===
 ['cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com']
'''
txt = 'Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'
print(find_all_emails(txt))


''' === RIGHT RESULT ===
['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']
'''
# txt = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# print(find_all_emails(txt))
