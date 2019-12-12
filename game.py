# -*- coding: UTF-8 -*-

import random

#auto函數：負責建立順序排列的牌堆
def auto():
    pokers=[]
    poker=[]
    for i in ['Heart','Spade','Diamond','Club']:
        for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
            poker=[]
    return pokers

def poker_game():
    player_name = []
    for i in range(player_number):
        player_name.append("player"+str(i))
    print ('玩家共有',player_number,'名','分別是：',player_name)

    li={}
    for k in player_name:
        b=random.sample(poker,2) #隨機抽兩張牌
        for s in b:
            poker.remove(s) #撲克牌被從牌堆裏抽出來
        li.setdefault(k,b)  #抽出來的撲克牌發給玩家
    print ('每個玩家抽到的牌爲：',li)

    temp2 = 0

    dic = {}
    tt_name = []

    for i in player_name:
        temp = 0
        for each in li[i]:
            if each[1] == 'A':
                temp = temp + 1
            elif each[1] == 'J':
                temp = temp + 11
            elif each[1] == 'Q':
                temp = temp + 12
            elif each[1] == 'K':
                temp = temp + 13
            else:
                temp = temp + int(each[1])
        print ('玩家',i,'抽到牌的總點數爲：',temp)
        if temp > temp2:
            temp2 = temp
            dic.setdefault(i, temp)
            tt_name.append(i)
        elif temp == temp2: #當前玩家總點數與之前的最大總點數一樣大的情況，先記錄下來
            dic.setdefault(i, temp)
            tt_name.append(i)

    for i in tt_name: #刪去之前記錄的不是最大的點數及其玩家姓名
        if dic[i] < temp2:
            del dic[i]
    print ('點數最大的玩家姓名及其點數爲：',dic)

while True:
    try:
        print ("\n———————————————新的一輪遊戲開始—————————————————\n")
        player_number = int(input("請輸入玩家的數量（輸入數字0則遊戲結束）: "))
        if player_number == 0:
            break
        elif player_number > 0 and player_number < 27: #除去大小王，有52張撲克牌，每人發兩張牌，最多26人蔘加遊戲
            poker = auto()
            print ('洗牌前：', poker)

            random.shuffle(poker)  # 洗牌

            print ('洗牌後：', poker)
            poker_game()
        else:
            print ("\n     !!! 請輸入正確的玩家數量！！！（必須是十進制數字，且大於0、小於27）")
    except:
        print ("\n     !!! 請輸入大於0、小於27的整數數字！！！")
        