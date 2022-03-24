import re
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

'''
arq = open(input('NAME OF FILE : '))
lista = list()
sum = 0
for line in arq:
    stuff = re.findall('([0-9]+)',line)
    if len(stuff) != 0:
        lista = lista + stuff
for i in lista:
    sum = int(i) + sum
'''

#print(len(lista))
#print(sum)
#
#
# representing simple strings
# print(ord('H'))
# >>>> 72
#
#

'''

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

'''

'''
greeet = '         Helllo bob     !     '
x = greeet.lstrip()
print(x)
x = greeet.rstrip()
print(x)
x = greeet.strip()
print(x)
y = greeet.split()
print(y)
'''
#relembrando o uso de split
#strip volta uma lista

# USING BEAUTIFUL BeautifulSoup
'''
import ssl
#
#IGNOARANDO POSSIVEIS ERROS
ctx = ssl.create_defaut_context()

ctx.check_hostname = False

ctx.verify_mode = ssl.CERT_NONE

url = input("ENTER:")
#BIG STRING COM A APGINA WEB
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tag = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''
