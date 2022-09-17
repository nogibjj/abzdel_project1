#!./venv/bin/python

import os
from databricks import sql

def querydb(query):

    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM default.fortune1000 LIMIT 2")
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result