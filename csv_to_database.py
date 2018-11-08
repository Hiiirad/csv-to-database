from csv import reader
import pyodbc
from time import sleep

database = "PostgreSQL35W" # check your odbc and put your DSN's database here
try:
    connection = pyodbc.connect(DSN=database, autocommit=True)
    print("\nDatabase connection has been established successfully.\n")
except Exception:
    print("Connection Failed, Check your connection with database.")
    exit()
finally:
    sleep(5)

row_num = 0
failed_num = 0
with open('final.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = reader(csvfile)
    next(csvreader) # ignore first row of csv which is header
    for row in csvreader:
        row_num += 1
        sql = "INSERT INTO pms.dim_knowledge_nw_tmp (id, event_category, event_title, event_id, starttime, recoverytime, impacted_object_type, impacted_object_name, impacted_district, impacted_service, cause_category, cause_description, suggestion, status, data_source, operator, impacted_object_value, last_update_activities, assignment_group, xpos, ypos, savetime, eventserialno, alarmlevel, lastalarmtime) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}'); commit;".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24])
        try:
            connection.execute(sql)
        except:
            failed_num += 1
            print("Could not execute SQL record #{0} :{1}".format(row_num,row))

# close the connectionection to the database.
connection.close()
print("\nTotal records are {0} and {1} records have been failed.\n".format(row_num,failed_num))
print("Done")
