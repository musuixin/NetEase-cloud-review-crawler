import requests
from bs4 import BeautifulSoup
import json
from tkinter import *
import os
def get_data():
    url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_'+v1.get()+'?csrf_token='
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    data={'params': 'N3C7dUFpElXdGq9beNXx3/WHEnBuB5bG2tIIiCuHyUmb66azM4YPU4bCRH/mDvt5hxOkBL1OpejK6/NFtDA1Z6EBWS52Rmj+ROpxBiAvIJv+Dlo0k3ophIQUZvqVUpqO3UTH23n2dGwEtgBVN2F7DClwOmGZdJoa5ELd/ndeKYtOM/3gBhIKJrzuuVuYoy5e',
    'encSecKey':'7ac494397bfd0554e4dc41c6fe9bc65b11f1d2f418e621982d735c6b77a02ea4b19578ffcb4c40a0b3e8fc006977d9c36fd91ace6faad92fa77e9d0fb7bb71bf9b2f99f16f25a11bf5eade19ccd70705a34bc78d487ef4372bbab9f72eed97afdca72a3552b3420e5ff4b2a886f0f7bcb71267e0f005d9c0e23a256705a819c0'}
    html=requests.post(url,headers=head,data=data)
    html=html.text
    data=json.loads(html)
    j=0
    os.chdir("e:\\网易云热评音乐")
    with open(v2.get()+".doc","w",encoding="utf-8") as f:
        for i in data['hotComments']:
            j+=1
            f.write((str(j)+".评论人名字:"+i['user']['nickname']+' 内容:'+i['content']+'\n'))
#创建窗口
root=Tk()
root.geometry('370x150+200+300')
#添加标题
root.title('网易云热评爬取by慕随心')
#添加标签(label)
label1=Label(root,font='微软雅黑',text="输入要爬取的音乐id:").grid(row=0)
label1=Label(root,font='微软雅黑',text="输入要爬取的音乐名称:").grid(row=1)
#添加输入框(entry)
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1).grid(row=0,column=1)
e1=Entry(root,textvariable=v2).grid(row=1,column=1)
#添加按钮(button)
button1=Button(root,font='微软雅黑',text='爬取',command=get_data).grid(row=3,column=0)
button2=Button(root,font='微软雅黑',text='退出',command=root.quit).grid(row=3,column=1)
#显示窗口
root.mainloop()


