from datetime import datetime
import psycopg2
from slugify import slugify
import pandas as pd
import re
db = psycopg2.connect(host='localhost',
                      user='veerinsta',
                      password='Wtx@135Gnt',
                      database='veerinsta$polynomials',
                      port='5432'
                      )


print('DB connected....')
cursor = db.cursor()
s=pd.read_csv(r"Culture.csv")
count1=0
category='Miscellanous'
sub_subject='Career Education'
for i in range(len(s.axes[0])):
    title=s['title'][i]
    headers=s['headers'][i]
    cont=s['content'][i]
    v=[]
    a=v.append   
    category_fetch_query = "SELECT sub_name FROM \"difference_between_category\" WHERE sub_name = \'"+category+"\'"
    cursor.execute(category_fetch_query)
    a = cursor.fetchone()
    if not a:
        category_insert = "INSERT INTO \"difference_between_category\" (sub_name) VALUES (%s)"
        value = (category,)
        cursor.execute(category_insert, value)
        db.commit()
    else:
        pass
    # file = open("Economics/{}.html".format(slugify(title)),"w",encoding="utf-8")
    # file.write('\n'.join(v))
    id_category_fetch = "SELECT id FROM \"difference_between_category\" WHERE sub_name = \'"+category+"\'"
    cursor.execute(id_category_fetch)
    category_id = cursor.fetchone()
    print(category_id)
    category_id = category_id[0]
    count1+=1
    category_insert = """INSERT INTO difference_between_differ VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    # category_insert='select count(*) from toppr_toppr'
    cursor.execute(category_insert,(count1,slugify(headers),title,headers,sub_subject,cont,category_id))
    db.commit()
    # # file.close()
