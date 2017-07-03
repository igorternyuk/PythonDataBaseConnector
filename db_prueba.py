from db_manager import *
DB_HOST = '127.0.0.1'
DB_USER = 'igor'
DB_PASS = '1319'
DB_NAME = 'db_persons'
def menu():
    m = DBManager(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    flag = True
    while flag:
        selector = input("****Database manager****\n1 - Insert;\n2 - Update;\n3 - Delete;\n4 - Custom select;\n5 - Select all;\n6- Search;\n7 -Quit;\n")
        if selector == 1:
            m.insert_data()
        elif selector == 2:
            m.update_data()
        elif selector == 3:
            m.delete_data()
        elif selector == 4:
            m.read_register()
        elif selector == 5:
            m.select_all_data();
        elif selector == 6:
            m.search_register();
        elif(selector == 7):
            flag = False
        else:
            continue
menu()
print "Good bye!"
