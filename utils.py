import psycopg2
def getConn():
    return psycopg2.connect("dbname='postgres' user='postgres' host='159.203.6.218' port='5432' password='eightgravity'")
