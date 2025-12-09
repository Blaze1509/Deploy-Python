import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def clear_table():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cursor = conn.cursor()
        table_name = os.getenv('TABLE_NAME', 'people')
        
        cursor.execute(f"DELETE FROM {table_name}")
        cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1")
        conn.commit()
        
        print(f"Table '{table_name}' cleared successfully")
        
        cursor.close()
        conn.close()
        
        return True, f"Table '{table_name}' cleared successfully"
        
    except Exception as e:
        error_msg = f"Error clearing table: {e}"
        print(error_msg)
        return False, error_msg

if __name__ == "__main__":
    clear_table()
