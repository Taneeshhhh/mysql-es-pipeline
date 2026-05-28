import mysql.connector
from elasticsearch import Elasticsearch
from config import MYSQL_CONFIG, ES_CONFIG
from datetime import datetime

# MYSQL CONNECTION
mysql_conn = mysql.connector.connect(**MYSQL_CONFIG)

cursor = mysql_conn.cursor(dictionary=True)

# ELASTICSEARCH CONNECTION
es = Elasticsearch(
    ES_CONFIG["url"],
    basic_auth=(
        ES_CONFIG["username"],
        ES_CONFIG["password"]
    ),
    verify_certs=False
)

# FETCH DATA
cursor.execute("SELECT * FROM student")
students = cursor.fetchall()
# CREATE "student" INDEX WITH TIMESTAMP MAPPING : NEEDED FOR GRAFANA visualization 
# PUT students
# {
#   "mappings": {
#     "properties": {
#       "ID": {
#         "type": "keyword"
#       },
#       "name": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword"
#           }
#         }
#       },
#       "dept_name": {
#         "type": "keyword"
#       },
#       "tot_cred": {
#         "type": "integer"
#       },
#       "@timestamp": {
#         "type": "date"
#       }
#     }
#   }
# }
# RUN THIS (ON KIBANA)

# PUSH TO ELASTICSEARCH
for student in students:

    # TRANSFORM THE DOCUMENT
    doc = {
        "ID": str(student["ID"]),
        "name": student["name"],
        "dept_name": student["dept_name"],
        "tot_cred": int(student["tot_cred"]),
        "@timestamp": datetime.utcnow().isoformat()
    }

    es.index(
        index="students",
        id=student["ID"],
        document=doc
    )

print("Data pushed successfully.")

# RUN THE DSL query:(on KIBANA)
# GET students/_search
# {
#   "query": {
#     "match_all": {}
#   }
# }
# WHICH Shows all the DOCUMENTS 

