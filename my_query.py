#https://stackoverflow.com/questions/24011428/django-core-exceptions-improperlyconfigured-requested-setting-caches-but-setti
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.db import connection


#https://djbook.ru/rel1.8/topics/db/sql.html
def my_custom_sql(query):
    cursor = connection.cursor()
    cursor.execute(query)
    #row = cursor.fetchone() #для получения одной строки
    rows = cursor.fetchall() #для получения всего результата
    return rows

# result = my_custom_sql("SELECT * FROM web_publication")
# for i in result:
#     print(i)

result = my_custom_sql("SELECT * FROM web_feedbacks")
for i in result:
    print(i)

