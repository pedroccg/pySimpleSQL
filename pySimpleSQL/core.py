import pandas as pd
import mysql.connector
from IPython.display import display, HTML, Markdown
import getpass

def display_library_documentation():
    documentation_md = """
      ## User Documentation

      ### Function: `setup_database`

      #### Description
      The `setup_database` function configures the database connection for SQL queries.
      It prompts the user to input their database credentials and other connection details interactively.
      This configuration is essential for establishing a connection to the database to execute SQL queries.

      #### Usage
      This function is typically invoked automatically when you first run a SQL query using `run_query`.
      However, it can also be manually called to reset or reconfigure the database connection details.

      #### Inputs
      - **Database Username**: The username for the database.
      - **Database Password**: The password for the database. (Input is hidden for security).
      - **Database Host**: The hostname or IP address of the database server.
      - **Database Name**: The name of the database to connect to.

      ---

      ### Function: `run_query`

      #### Description
      The `run_query` function is used to execute SQL queries on the configured database. It supports executing multiple queries in a single call.
      The function automatically handles different types of SQL statements including `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and others.

      #### Usage
      Write your SQL query or queries as a string. If executing multiple queries, separate them with a semicolon (`;`).
      The function will execute each query in sequence and display the results for `SELECT` queries or a success message for other types of queries.

      #### Inputs
      - **query**: A string containing the SQL query or queries to be executed.
    """

    display(Markdown(documentation_md))


def set_db_config(custom_config):
    global db_config
    db_config = custom_config

def setup_database():
    db_user = getpass.getpass('Enter Database Username: ')
    db_password = getpass.getpass('Enter Database Password: ')
    db_host = input('Enter Database Host: ')
    db_name = input('Enter Database Name: ')
    db_config = {
        'user': db_user,
        'password': db_password,
        'host': db_host,
        'database': db_name
    }
    set_db_config(db_config)

def get_db_config():
    global db_config
    if not db_config:
        db_config = setup_database()
    return db_config

def styled_print(message, color='black', font_size='14px'):
    display(HTML(f"<p style='color: {color}; font-size: {font_size};'>{message}</p>"))

def run_query(query):
    db_config = get_db_config();
    try:
        with mysql.connector.connect(**db_config) as cnx:
            with cnx.cursor() as cursor:
                statements = query.strip().split(';')
                for i, statement in enumerate(statements, start=1):
                    if statement.strip():
                        cursor.execute(statement)
                        if cursor.description:
                            column_names = [i[0] for i in cursor.description]
                            df = pd.DataFrame(cursor.fetchall(), columns=column_names)
                            styled_print(f"Result of Query {i}:", font_size='16px', color='green')
                            display(df)
                        else:
                            styled_print(f"Query {i} executed successfully. Rows affected: {cursor.rowcount}", font_size='14px', color='green')
                        cnx.commit()
    except mysql.connector.Error as e:
        styled_print(f"Error in Query {i}: {e}", color='red')
    finally:
        if cnx.is_connected():
            cnx.close()