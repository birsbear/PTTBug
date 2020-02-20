# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:01:37 2020

@author: mini01
"""

import requests
from bs4 import BeautifulSoup

def calcul_page(content):
    pre_index = content.index('/index')+6
    pro_index = content.index('.html')
    page = int(content[pre_index:pro_index])
    
    return page

if __name__ == "__main__" :
    page_num = 2
    board_dict = {
                '1':['01.八卦',"Gossiping"], 
                '2':['02.台中', 'TaichungBun'], 
                '3':['03.魔物獵人', 'MH'],
                '4':['04.程式接案', 'CodeJob'],
                '5':['05.SOHO', 'soho'],
                '6':['06.資料科學', 'DataScience'],
                '7':['07.馬佛', 'marvel'],
                '8':['08.手作', 'HandMade'],
                '9':['09.家教', 'HomeTeach'],
                '10':['10.基金', 'Fund'],
                '11':['11.股票', 'Stock'],
                '12':['12.海外投資', 'Foreign_Inv'],
                '13':['13.組合語言', 'ASM'],
                '14':['14.防毒', 'AntiVirus'],
                '15':['15.C&C++', 'C_and_CPP'],
                '16':['16.Python', 'Python'],
                '17':['17.科技工作', 'Tech_Job'],
                '18':['18.軟體工作', 'Soft_Job'],
                '19':['19.海外工作', 'Oversea_Job']
            }
    for i in board_dict:
        print(board_dict[i][0], end=' ')
    board = input("請輸入看板代號 : ")
    board_index = board.split(',')
    for board_num in board_index:
        board_url = board_dict[board_num][1]
        
        url = 'https://www.ptt.cc/bbs/' + board_url + '/index.html'
        
        ptt_u = requests.get(url)
        content = BeautifulSoup(ptt_u.text, features="lxml")
        board_page = calcul_page(content.select('.btn.wide')[1]['href'])+1
        #print("最大頁數:"+str(board_page))
        print("你正處在"+board_url+'版')
        for j in range(page_num,0,-1):
            current_url = 'https://www.ptt.cc/bbs/' + board_url + '/index'+str(board_page-j+1)+'.html'
            current_web = requests.get(current_url)
            current_content = BeautifulSoup(current_web.text, features="lxml")
            for entry in current_content.select('.r-ent'):
                if "本文已被刪除" in entry.select('.title')[0].text:
                    print(entry.select('.title')[0].text.replace('\n\t\t\t',''))
                else:
                    print(entry.select('.nrec')[0].text,'\t',entry.select('.title')[0].text.replace('\n', ''),entry.select('.date')[0].text,entry.select('.author')[0].text)
        print('*********************************************************')