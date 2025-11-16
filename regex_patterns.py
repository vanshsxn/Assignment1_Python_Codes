import re

patterns={
"Indian Mobile":re.compile(r"(?:\+91[\-\s]?|0)?[6-9]\d{9}\b"),
"PAN":re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b",re.I),
"Aadhaar":re.compile(r"\b\d{4}\s?\d{4}\s?\d{4}\b"),
"Postal PIN":re.compile(r"\b[1-9]\d{5}\b"),
"URL":re.compile(r"\b(?:https?://)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:/[-a-zA-Z0-9()@:%_\+.~#?&/=]*)?"),
"IPv4":re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b"),
"Strong Password":re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
}

sample_text=\"\"\"
Contact: +91-9876543210 or 09876543210 or 912345678901
PAN: ABCDE1234F
Aadhaar: 1234 5678 9123
PIN: 110001
Website: https://www.example.com/path?q=1
Server: 192.168.1.100
Try password: StrongP@ss1
Another mobile: 9123456789
\"\"\"

results={}
for name,pat in patterns.items():
    if name=="Strong Password":
        for tok in sample_text.split():
            if pat.match(tok):
                results.setdefault(name,[]).append(tok)
    else:
        results[name]=pat.findall(sample_text)

for k,v in results.items():
    print(k, "->", v)
