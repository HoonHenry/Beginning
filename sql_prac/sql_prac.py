import pymysql
import csv
import pandas as pd

conn = pymysql.connect(host='localhost', user='root',
                       password='%!*^1826dHsong',
                       db='opentutorial', charset='utf8',
                       autocommit=True)

curs = conn.cursor()

#curs.execute("CREATE TABLE goobne_store (id INT AUTO_INCREMENT PRIMARY KEY, store_name VARCHAR(40), address TEXT)")
#print("a")
file = 'D:\\HoonsCode\\Beginning\\crawling\\table_goobne.csv'
csv_data = pd.read_csv(file)
# print("b")
# print(type(csv_data))
# print(csv_data)

for count in range(len(csv_data)):
    # print("c")
    # print(row)
    try:
        row1 = count
        row2 = str(csv_data["name"][count])
        row3 = str(csv_data["address"][count])
        print(type(row1), type(row2), type(row3))
        query = """INSERT INTO goobne_store(id, store_name,
        address) VALUES(%d, '%s', '%s')""" % (row1, row2, row3)
        # print(query)
        curs.execute(query)

    except Exception as e:
        print(e)
        print(row1, row2)
        continue

    # curs.execute("""INSERT INTO goobne_store(store_name,
    #  address)" "VALUES('%s', '%s')""", row)
    # print("d")

# print("passed")
# rows = curs.fetchall()
# #conn.commit()
# curs.close()
# print(rows[0:3])
# print("The end")

