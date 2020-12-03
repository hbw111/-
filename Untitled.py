
# coding: utf-8

# In[ ]:


def move(list1,step):
    #移动step前的元素到列表的末尾
    num = step-1
    while num > 0:
        tmp = list1.pop(0)
        list1.append(tmp)
        num = num - 1
        
    return list1 #根据step做了元素的移动

def play(players,step,alive):

    #生成一个列表，从【1、、、players】
    list1 =[i for i in range(1,players+1)]
    
    #进入游戏的循环，每次数到step淘汰，step之前的元素要移动到末尾
    #游戏结束的条件是，列表剩余人数小雨alive
    while len(list1)>alive:
        list1=move(list1,step)
        
        list1.pop(0)

    return list1

players_num = int(input("请输入参加游戏的人数"))
step_num = int(input("请输入淘汰的数字"))
alive_num = int(input("请输入幸存的数字"))

alive_list = play(players_num,step_num,alive_num)
print(alive_list)

