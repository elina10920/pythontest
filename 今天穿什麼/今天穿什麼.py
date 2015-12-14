
# coding: utf-8

# In[ ]:

while True:
    tem= int(input("請輸入溫度"))
    if 14 > tem :
        print("毛帽、圍巾、口罩、兩件以上長袖衣服、長褲")
    elif 14 <= tem < 18:
        print("毛帽、圍巾、兩件長袖衣服、長褲")
    elif 18 <= tem < 22:
        print("薄外套、一件長袖衣服、長褲")
    elif 22<= tem <24:
        print("一件短袖衣服、長褲")
    else:
        print("一件短袖衣服、短褲")

