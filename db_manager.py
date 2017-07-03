import MySQLdb

class DBManager(object):
    def __init__(self, host, user, password, db_name):
        self.__db_host = host
        self.__db_user = user
        self.__db_pass = password
        self.__db_name = db_name

    def __run_query__(self, query=''):
        datos = [self.__db_host, self.__db_user,
                 self.__db_pass, self.__db_name]
        data = None
        conn = None
        cursor = None
        try:
            conn = MySQLdb.connect(*datos)
            cursor = conn.cursor()
            cursor.execute(query)
            if(query.upper().startswith('SELECT')):
                data = cursor.fetchall()
            else:
                conn.commit()
        finally:
            cursor.close()
            conn.close()
            return data

    def insert_data(self):
        print "***Insert date***"
        name = raw_input("Type name of person:\n")
        tel = input("Type phone number:\n")
        query = "INSERT INTO persons values(default,'%s',%i);" % (name,int(tel))
        print "SQL =", query
        self.__run_query__(query)

    def update_data(self):
        print "***Update data***"
        id = input("Specify id of register:\n")
        name = raw_input("Name:\n")
        tel = input("Tel:\n")
        query = "UPDATE persons SET name ='%s',phone=%i WHERE id = %i;" % (name, tel, id)
        print "SQL =",query
        self.__run_query__(query)

    def delete_data(self):
        print "***Delete data***"
        id = input("Specify id to delete:\n")
        query = "DELETE FROM persons WHERE id = %i" % id
        print "SQL=", query
        self.__run_query__(query)

    def select_all_data(self):
        print "***All registers***"
        query = "SELECT * FROM persons ORDER BY name DESC;"
        resultSet = self.__run_query__(query)
        print resultSet[0]
        print "size =",len(resultSet)
        for i in resultSet:
            print i,"\n"

    def read_register(self):
        print "***Reading register by ID***"
        id = input("Specify id for reading:")
        query = "SELECT * FROM persons WHERE id = %i;" % id
        resultSet = self.__run_query__(query)
        for i in resultSet:
            print i,"\n"
        #for line in resultSet
        #    print line,"\n"

    def search_register(self):
        print "***Searching register***"
        regExp = raw_input("Type search pattern:\n")
        regExp = "%" + regExp + "%"
        query = "SELECT * FROM persons WHERE name like '%s';" % regExp
        print "SQL=",query
        resultSet = self.__run_query__(query)
        print resultSet[0]
        for i in resultSet:
            print i,"\n"
