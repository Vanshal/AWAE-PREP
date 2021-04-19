 The following are some of the main sinks that can lead to DOM-XSS vulnerabilities:
 
Source: https://portswigger.net/web-security/cross-site-scripting/dom-based

```
document.write()
document.writeln()
document.domain
someDOMElement.innerHTML
someDOMElement.outerHTML
someDOMElement.insertAdjacentHTML
someDOMElement.onevent
```

To find if any of the sinks is used in html files:

```
while read l; do echo "--------$l-------";egrep -n "document.write\(|document.writeln\(|document.domain|innerHTML|outerHTML|insertAdjacentHTML|onevent" $l ;done < html_files
```

