import os
import re
import sqlite3
import pandas as pd

"""
    See:
        https://www.census.gov/topics/population/genealogy/data/2010_surnames.html
"""
CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'Names_2010Census.csv')
SQL_PATH = os.path.join(os.environ["HOME"], '.lastname.sqlite')


class LastName:

    db = None

    def __init__(self):
        if not os.path.exists(SQL_PATH):
            if not os.path.exists(CSV_PATH):
                raise Exception(f'Missing CSV at: {CSV_PATH}')
            self._create_db_()
        else:
            self.db = sqlite3.connect(SQL_PATH)


    def _create_db_(self):
        self.db = sqlite3.connect(SQL_PATH)
        c = self.db.cursor()
        users = pd.read_csv(CSV_PATH)
        users.to_sql('names', self.db, index = False)


    def lookup(self, name):

        if not isinstance(name, str):
            raise Exception(f'lookup requires name parameter as str')

        name = re.sub(r'[^A-Z]+', "", name.upper().strip())

        if len(name) == 0:
            return None

        c = self.db.cursor()

        c.execute(f"SELECT * FROM names WHERE name = '{name}' LIMIT 1")

        row = c.fetchone()

        if row is None:
            return None

        row = list(row)
        cols = [col[0] for col in c.description]

        c.close()

        return {col: row.pop(0) for col in cols}

