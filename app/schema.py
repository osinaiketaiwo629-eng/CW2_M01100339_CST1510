import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sqlite3
from db_management import create_user_table

if __name__ == "__main__":
     conn = sqlite3.connect('DATA/telligence_platform.db')
     create_user_table(conn)
     conn.close()
     



