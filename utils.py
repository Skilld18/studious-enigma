import psycopg2


def sql(query, data=None):
    con = psycopg2.connect("dbname='postgres' user='postgres' host='159.203.6.218' port='5432' password='eightgravity'")
    cur = con.cursor()
    cur.execute(query, data)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result

def get_all_rows(database, dataType):
    return map(lambda x: dataType(*x), sql("SELECT * FROM " + database))

def get_items(criteria, all_items):
    return filter(criteria, all_items)

# Wrappers
def get_by_key(key, elements):
    for item in get_items(lambda x: key_match(x, key), elements):
        return item

# Criteria
def key_match(element, key):
    return element.key == key

