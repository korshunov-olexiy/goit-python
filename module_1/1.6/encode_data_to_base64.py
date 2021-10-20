import base64


def encode_data_to_base64(data):
    data64 = []
    for credential in data:
        data64.append(base64.b64encode(credential.encode()).decode())
    return data64

l = ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(l))