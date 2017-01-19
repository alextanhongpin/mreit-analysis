import sqlite3 as sql

def select_reit_by_name (name, sort_by='name'):
  with sql.connect('mreit.db') as conn:
    # Now we can access the result
    # with reit['date'] == reit[0] == reit['DaTE']
    print(sort_by)
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    result = cursor.execute('SELECT * FROM mreit WHERE name=? ORDER BY cast(? as SIGNED) ASC', (name, sort_by,))
    # conn.close()
    return result.fetchall()

def select_reit_to_csv (name):
  with sql.connect('mreit.db') as conn:
    cursor = conn.cursor()
    result = cursor.execute('SELECT * FROM mreit WHERE name=?', (name,))
    # conn.close()
    return result.fetchall()

def select_reits ():
  with sql.connect('mreit.db') as conn:
    # Now we can access the result
    # with reit['date'] == reit[0] == reit['DaTE']
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    result = cursor.execute('SELECT DISTINCT name FROM mreit ORDER BY name ASC')
    # conn.close()
    return result.fetchall()

def select_reits_by_date (date, sort_by='name'):
  with sql.connect('mreit.db') as conn:
    # Now we can access the result
    # with reit['date'] == reit[0] == reit['DaTE']
    conn.row_factory = sql.Row
    print('at slecte reits by date')
    print(sort_by)
    cursor = conn.cursor()
    result = cursor.execute('''
      SELECT * FROM mreit
      WHERE date=?
      ORDER BY ? ASC;'''
      , (date, sort_by,))
    # conn.close()
    return result.fetchall()