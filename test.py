# -*- coding:utf-8 -*-

import numpy as np 

import pandas as pd

import csv


print("hello world, Jiangbo")

#print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

#conductexcel.openlist("20160101-1230.xlsx")

def sort_by_value(d, rever = False ): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse = rever ) 
    return [ backitems[i][1] for i in range(0,len(backitems))] 

#将二层List写入一个csv文件中
#
def createListCSV(fileName="", dataList=[]):
    with open(fileName, "w",encoding='utf8',newline='') as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=' ')
        for data in dataList:
            print(data)
            csvWriter.writerow(data)
        csvFile.close

#将Dict数据写入一个csv文件中
#
def createDictCSV(fileName="", dataDict={}):
    with open(fileName, "w",encoding='utf8',newline='') as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=' ')
        for data in dataDict:  
            print(data)
            csvWriter.writerow(data)
        csvFile.close()

d1 = { '000001':[3129.3], '600050':[7.08], '601118':[7.32] }


print(d1)

#print(d1.iteritems())

#createDictCSV(fileName="secu0227.csv", dataDict=d1)

#按value排序
d1 = sort_by_value(d1, rever= True)

print(d1)

"""
writer = csv.writer(open('your.csv', 'w',encoding='utf8',newline=''))
writer.writerow(['Column1', 'Column2', 'Column3'])
lines = [range(3) for i in range(5)]
for line in lines:
    writer.writerow(line)
"""

#createListCSV("sortedsecu0509.csv", d1)


b=np.array( [ (1.5,2,3), (4,5,6) ] )

print(b)

df = pd.DataFrame(b)

print(df)

#df.to_excel("temp.xlsx", "temp")    #经过第三方安装包的引入，写入excel成功

print(df.describe().max())

#df = pd.read_csv("C:\Users\lwx10116\Downloads\one.csv",encoding='gb2312')


#print(df)

colname_price = ['三日前收盘','两日前收盘','昨收盘','今收盘','今涨幅','5天前收盘','5天涨幅', '22天前收盘','22天涨幅','证券名']

colname_newstocks =['display_name','name','start_date','end_date','type']

filename_price = 'C:\\Users\\lwx10116\\Downloads\\每日复盘收盘价.csv'   #需要使用\\转义符号

filename_volumn = 'C:\\Users\\lwx10116\\Downloads\\每日复盘成交量.csv'

filename_newstocks = 'C:\\Users\\lwx10116\\Downloads\\新上市股表.csv'


#读入dataframe导出的csv文件，生成新的dataframe对象, 使用新的列名代替原来的列名
df_today_price = pd.read_csv(filename_price, header=0, names = colname_price, sep=',', encoding='utf_8')  

df_newstocks = pd.read_csv(filename_newstocks, header=0, names = colname_newstocks, sep=',', encoding='utf_8')  

#df_today_column = pd.read_csv(filename_volumn, header=0, names = colname, sep=',', encoding='utf_8')  

#print(df_today_price)

#找出当天涨停和跌停的，按涨幅降序排列
todayzhangting = df_today_price[(df_today_price['今涨幅']>=0.0997)]

todayzhangting.sort_values('今涨幅',ascending=False)

CntZhangting = len(todayzhangting)
#print('涨停家数: ', CntZhangting)

todaydieting = df_today_price[(df_today_price['今涨幅'] <= -0.0997)]
todaydieting.sort_values('今涨幅',ascending=False)

CntDieting = len(todaydieting)
#print('跌停家数: ', CntDieting)


#找出当天涨幅在[5, 涨停)，或（跌停，-5]间，按涨幅降序排列， 即除掉涨跌停，涨跌幅度在5个点以上的。
today5up = df_today_price[(df_today_price['今涨幅'] >= 0.05) & (df_today_price['今涨幅'] < 0.0997)]
today5up.sort_values('今涨幅',ascending=False)

Cnt5up = len(today5up)
#print('涨幅大于5个点家数: ', Cnt5up)

today5down = df_today_price[(df_today_price['今涨幅'] <= -0.05) & (df_today_price['今涨幅'] > -0.0997)]
today5down.sort_values('今涨幅',ascending=False)

Cnt5down = len(today5down)
#print('跌幅大于5个点家数: ', Cnt5down)


#找出当天涨幅在[1,5), 或(-5,-1]间， 按张幅降序排列，即涨幅在1到5个点间的
todaysmallup = df_today_price[(df_today_price['今涨幅'] >= 0.01) & (df_today_price['今涨幅'] < 0.05)]
todaysmallup.sort_values('今涨幅',ascending=False)

CntSmallup = len(todaysmallup)
#print('涨幅在1到5个点家数: ', CntSmallup)

todaysmalldown = df_today_price[(df_today_price['今涨幅'] > -0.05) & (df_today_price['今涨幅'] <= -0.01)]
todaysmalldown.sort_values('今涨幅',ascending=False)

CntSmalldown = len(todaysmalldown)
#print('跌幅在1到5个点家数: ', CntSmalldown)

#找出当天涨幅在(-1,1)间的，即在横盘状态的
todayhengpan = df_today_price[(df_today_price['今涨幅'] > -0.01) & (df_today_price['今涨幅'] < 0.01)]
todayhengpan.sort_values('今涨幅',ascending=False)

CntHengpan = len(todayhengpan)
#print('横盘家数: ', CntHengpan )

aa={'数量':[CntZhangting, CntDieting, Cnt5up, Cnt5down, CntSmallup, CntSmalldown, CntHengpan]}

df_todayresult = pd.DataFrame(aa,index=['涨停家数','跌停家数','涨幅大于5个点','跌幅大于5个点','涨幅在1到5之间','跌幅在1到5之间','横盘家数'])

print(df_todayresult)

#找出新股列表，单独标识为一列
df_today_price['是否新股'] = '否'

#print(df_today_price)

try:
    df_today_price.loc[list(df_newstocks.index),['是否新股']] = '是'    #这里要加一个异常处理，捕获查找不到的异常
except KeyError:
    print(KeyError)
       

#获取一个已存在的excel文件，在已有文件上写入不同的dataframe
excelwriter = pd.ExcelWriter('每日分析.xlsx')
#写入Excel表文件中，不同的sheet页
df_today_price.to_excel(excelwriter, "收盘数据")

#找出新股列表，单独标识为一列

    
todayzhangting.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"今涨停")

todaydieting.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"今跌停")

today5up.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"涨幅大于5个点")

today5down.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"跌幅大于5个点")

todaysmallup.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"涨幅在1到5之间")

todaysmalldown.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"跌幅在1到5之间")

todayhengpan.sort_values('今涨幅',ascending=False).to_excel(excelwriter,"横盘")

df_todayresult.to_excel(excelwriter, "统计结果")

df_today_price.sort_values('22天涨幅',ascending=False).head(20).to_excel(excelwriter, "22天涨幅TopN")

df_today_price.sort_values('5天涨幅',ascending=False).head(20).to_excel(excelwriter, "5天涨幅TopN")

excelwriter.save()

#将22日涨幅和5日涨幅的TopN，除掉新股列表，存成txt文件

list22dayTopN = df_today_price.sort_values('22天涨幅',ascending=False).head(20)[df_today_price['是否新股']=='否'].index.tolist()

list5dayTopN = df_today_price.sort_values('5天涨幅',ascending=False).head(20)[df_today_price['是否新股']=='否'].index.tolist()

list5dayTopN = [ stockcode[0:6] for stockcode in list5dayTopN]  

list22dayTopN = [ stockcode[0:6] for stockcode in list22dayTopN]

print(list22dayTopN)
print(list5dayTopN)

fl=open('5天涨幅靠前.txt', 'w')
for i in list5dayTopN:
    fl.write(i)
    fl.write("\n")
fl.close()

f2=open('22天涨幅靠前.txt', 'w')
for i in list22dayTopN:
    f2.write(i)
    f2.write("\n")
f2.close()


#print(df_newstocks)


