import sqlite3
import pandas as pd

def sqlite_to_csv(db_path: str, table_name: str, csv_path: str) -> None:
    try:
        conn = sqlite3.connect(db_path)

        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)

        df.to_csv(csv_path, index=False)

        print(f"Success! Table '{table_name}' exported to '{csv_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if "conn" in locals():
            conn.close()

if __name__ == "__main__":
    pass