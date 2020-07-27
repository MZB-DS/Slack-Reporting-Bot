import pandas as pd
import mysql.connector

def get_data(query,columns_list):

  mydb = mysql.connector.connect(
    host='host_ip', # Enter your mysql host ip here
    user='username', # Enter your mysql username
    passwd='password', # Enter mysql password
    database='default_database' # Enter any database name
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
