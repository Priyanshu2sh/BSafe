import base64

with open("C:\\Users\\ps200\\Desktop\\Prushal Tech\\BSafe\\bsafe\\myapp\\a.png", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")

print(encoded)
