import requests

url='https://jsonplaceholder.typicode.com/posts'
x=requests.get(url)

print(x.cookies)