import pandas as pd
import mysql.connector
from IPython.display import display

def run_query(query, db_config):
        with mysql.connector.connect(**db_config) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(query)
            # For SELECT queries, fetch the results and return a DataFrame
            if query.strip().upper().startswith('SELECT'):
                column_names = [i[0] for i in cursor.description]
                result = pd.DataFrame(cursor.fetchall(), columns=column_names)
                display(result)
            else:
                # For non-SELECT queries, commit the changes to the database
                cnx.commit()
                return None
            cursor.close()
            cnx.close()