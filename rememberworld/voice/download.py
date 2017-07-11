import requests
orda = ord('a')
ordz=ord('z')
for i in range(orda,ordz+1):
    url = 'http://images.juren.com/file/20090804/'+chr(i)+'.rar'
    print url
    r=requests.get(url)
    if r.status_code == 200:
        with open(url.split(r'/')[-1],'wb') as f:
            f.write(r.content)
            print 'finish' , url
