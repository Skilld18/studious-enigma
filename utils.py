import psycopg2

def sql(query, data = None):
    con = psycopg2.connect("dbname='postgres' user='postgres' host='159.203.6.218' port='5432' password='eightgravity'")
    cur = con.cursor()
    cur.execute(query, data)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result
