import psycopg2

con = None
cur = None


def sql(query, data=None):
    global con, cur
    result = []
    if not con:
        con = psycopg2.connect(
            "dbname='postgres'\
            user='postgres'\
            host='159.203.6.218'\
            port='5432' \
            password='eightgravity'")
        cur = con.cursor()
    cur.execute(query, data)
    # Fix this
    if query[0:6].upper() == "SELECT":
        result = cur.fetchall()
    # Needed for upsert
    con.commit()
    return result


# This may need to be placed in the implemented classes
def get_all_rows(database, data_type):
    return map(lambda x: data_type(*x), sql("SELECT * FROM  " + database))


def get_items(criteria, all_items):
    return filter(criteria, all_items)


# Wrappers
def by_key(key, elements):
    for item in get_items(lambda x: key_match(x, key), elements):
        return item


def update_answer(answer_key, question_key, string):
    data = (answer_key, question_key, string)
    sql("""
    INSERT INTO answers(key, questionKey, userKey, answer)
    VALUES (DEFAULT, %s, %s, %s)
    ON CONFLICT (questionKey, userKey) DO UPDATE SET answer = EXCLUDED.answer;
    """, data)


# Criteria
def key_match(element, key):
    return element.key == key

