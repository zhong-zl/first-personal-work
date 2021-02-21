import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
}
sou='1613797084480'
cursor='0'

result_list = []
result_list1=[]

for i in range(0,1000):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+data1
    source = requests.get(url, headers=headers).content.decode()
    result_list= re.findall('.*?content":"(.*?),"',source,re.S)
    result_list1.append(result_list)
    cursor=re.findall('.*?"last":"(.*?)"',source,re.S)[0].replace(" ","").replace("\n","")
    sou=str(int(sou)+1)


with open('评论.txt', 'a' , encoding='utf-8') as file:
    file.write(str(result_list1))