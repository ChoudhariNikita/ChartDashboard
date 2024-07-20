import json
import mysql.connector
from dateutil import parser

# Load JSON data with explicit encoding specification
with open('data/jsondata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

try:
    con = mysql.connector.connect(
        user='root',
        password='adminroot@123',
        host='localhost',
        port=3306,
        database='dashboard_db'
    )
    if con.is_connected():
        print('connected')
except Exception as e:
    print("Cannot connect:", e)

cur = con.cursor()

for item in data:
    # Convert empty strings to None
    added = parser.parse(item['added']) if item['added'] else None
    published = parser.parse(item['published']) if item['published'] else None
    
    values = (
        item['title'],
        item['sector'],
        item['topic'],
        item['insight'],
        item['url'],
        item['region'],
        item['start_year'] if item['start_year'] else None,
        item['end_year'] if item['end_year'] else None,
        item['impact'] if item['impact'] else None,
        added,
        published,
        item['country'],
        item['relevance'] if item['relevance'] else None,
        item['pestle'],
        item['source'],
        item['likelihood'] if item['likelihood'] else None,
        item['intensity'] if item['intensity'] else None
    )
    
    sql = """
    INSERT INTO energy_outlook (
        title, sector, topic, insight, url, region, start_year, end_year, impact, added, published, country, relevance, pestle, source, likelihood, intensity
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, values)
    con.commit()
    print(cur.rowcount, "record inserted")

cur.close()
con.close()
