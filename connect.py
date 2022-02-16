import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        postgreSQL_select_Query = 'SELECT * FROM power_energydata WHERE id=(SELECT max(id) FROM power_energydata)'
        
        
    # execute a statement
       
        cur.execute('SELECT version()')
        cur.execute(postgreSQL_select_Query)

        # display the PostgreSQL database server version
        #db_version = cur.fetchone()
        latest_record = cur.fetchone()

        #print('PostgreSQL database version:')
        #print(db_version)
        print("Latest Data Fetched")
        print(latest_record)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()