import pandas as pd
import mysql.connector

def get_data(query,columns_list):

  mydb = mysql.connector.connect(
    host='host_ip',
    user='username',
    passwd='password',
    database='default_database'
  )

  mycursor = mydb.cursor()

  final_list = list()

  mycursor.execute(query)

  myresult = mycursor.fetchall()

  for x in myresult:
    final_list.append(list(x))

  SQL_Dataframe = pd.DataFrame(final_list,columns=columns_list)
  mycursor.close()
  mydb.close()
  return SQL_Dataframe
