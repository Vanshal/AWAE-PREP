To Match Between two: string,character,word. eg: Random "test" "test23"

To print the first occurrence of word between quotes.

Regex with python:
  
  ```re.match('\"(.*?)\"',allstrings)```
  
  ```print(re.match('\"(.*?)\"',allstrings).group())```

* REPLACE **match** with **findall** to find all words between quotes ie: test test23
* this regex will only print in-between the given string it will not print the given string in this case it will not print the quotes 

To Match Between Multiline

eg:
```
123
TEST
asd
<name>
qwe
JOHN
qq
</name>
rwq
```

```print(re.findall("name([\S\s]*?)name",multiline_var))```

**output will contain: qwe john qq**

