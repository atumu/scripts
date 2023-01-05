from urllib.request import urlopen
ip = urlopen('http://ip.42.pl/raw').read().decode()
## 打印
print(ip)




