import numpy as np
import pandas as pd
from lxml import objectify
from pandas.io.json import json_normalize
import json
from pandas.io.pytables import HDFStore
import pickle
from sqlalchemy import create_engine

csvframe = pd.read_csv('myCSV_01.csv')
csvframe1 = pd.read_csv('myCSV_02.csv',header=None)
csvframe2 = pd.read_csv('myCSV_03.csv',index_col=['color','status'])
txtframe = pd.read_table('ch05_04.txt',sep='\s+')
txtframe1 = pd.read_table('ch05_05.txt',sep=r'\D+',header=None,engine='python')
txtframe2 = pd.read_table('ch05_06.txt',sep=',',skiprows=[0,1,3,6])
a = pd.read_csv('myCSV_02.csv',skiprows=[2],nrows=2,header=None)
print()
out = pd.Series()
pieces = pd.read_csv('myCSV_01.csv',chunksize=3)
i = 0
for piece in pieces:
    print(piece['red'])
    out.at[i] = piece['red'].sum()
    i += 1
print()
frame2 = pd.read_csv('ch05_07.csv')
frame2.to_csv('ch05_07_1.csv')
frame2.to_csv('ch05_07_2.csv',index=False,header=False)
frame3 = pd.read_csv('ch05_08.csv')
frame3.to_csv('ch05_08_1.csv')
frame3.to_csv('ch05_08_2.csv',na_rep='NaN')
frame1 = pd.DataFrame(np.random.random((4,4)),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame1.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)
html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()
web_frames = pd.read_html('myframe.html')
ranking = pd.read_html('http://www.meccanismocomplesso.org/en/'
                       'eccanismo-complesso-sito-2/classifica-punteggio/')
print(ranking[0][1:10])
xml = objectify.parse('Books.xml')
root = xml.getroot()
print(root.Book.Author)
mes1 = root.Book.getchildren()
print(mes1)
print([child.tag for child in mes1])
print([child.text for child in mes1])
xlsframe = pd.read_excel('data.xlsx',1)
print(xlsframe)
frame = pd.DataFrame(np.random.random((4,4)),
                     index=['exp1','exp2','exp3','exp4'],
                     columns=['Jan2015','Fab2015','Mar2015','Apr2005'])
frame.to_excel('data2.xlsx')
frame5 = pd.DataFrame(np.arange(16).reshape(4,4),
                      index=['white','black','red','blue'],
                      columns=['up','down','right','left'])
print(pd.read_json('frame.json'))
file = open('books.json','r')
text = file.read()
text = json.loads(text)
b = json_normalize(text[0],'books','writer')
print(b)
store = HDFStore('mydata.h5')
store['obj1'] = frame5
print(store['obj1'])
data = {'color':['white','red'],'value':[5,7]}
pickled_data = pickle.dumps(data)
print(pickled_data)
nframe = pickle.loads(pickled_data)
print(nframe)
frame5 = pd.DataFrame(np.arange(20).reshape(4,5),
                      columns=['white','red','blue','black','green'])
engine = create_engine('sqlite:///foo.db')
frame5.to_sql('a',engine)
print(pd.read_sql('a',engine))
