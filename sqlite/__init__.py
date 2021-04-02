import sqlite3

# connect to database on startup / create if doesnt exist



class sqliteDB():
    def __init__(self):
        # connect to local db
        self.con = sqlite3.connect('data.db')
        # create cursor for sqlite
        self.cur = self.con.cursor()

    def _create_table(self):
        # Create table price-data
        query = "CREATE TABLE " + "price_data" + " (date text, exchange text, pair text, value real)"
        self.cur.execute(query)

    def _table_exists(self):
        # if this is first run, create table
        self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='price_data' ''')

        # if the count is 1, then table exists
        if self.cur.fetchone()[0] == 1:
            print('Table exists, continuing.')
        else:
            print('Creating table.')
            self._create_table()
            print('Table created.')

    def insert_record(self, datetime, exchange, pair, value):
        # Insert a row of data
        query = "INSERT INTO price_data VALUES('" + str(datetime) + "', '" + str(exchange) + "', '" + pair + "', " + str(value) + ")"
        self.cur.execute(query)
        # save changes by committing them
        self.con.commit()




