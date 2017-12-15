import psycopg2

DBNAME = 'news'

try:
    conn = psycopg2.connect(database=DBNAME)
except:
    print "I am unable to connect to the database."
    cursor = conn.cursor()

cursor = conn.cursor()

cursor.execute(
    """SELECT articles.title as articles, count(log.id) as views
    FROM log JOIN articles ON log.path
    LIKE '%'||articles.slug||'%'
    GROUP BY articles.title
    ORDER BY views DESC LIMIT 3""")

results = cursor.fetchall()

print "Top 3 Articles"
for row in results:
    print "  ", row[0], " ", row[1], "-", "views"
print '\n'
cursor.execute(
    """SELECT authors_slug.authors AS authors, COUNT(log.id) AS views
    FROM log JOIN authors_slug ON log.path
    LIKE '%'||authors_slug.slug||'%'
    GROUP BY authors_slug.authors
    ORDER BY views;""")

results = cursor.fetchall()
print "Most Popular Authors"

for row in results:
    print "  ", row[0], " ", row[1], "-", "views"
print '\n'

cursor.execute(
    """SELECT date, percent_error
    FROM day_percent_error
    WHERE percent_error >= 1;""")

results = cursor.fetchall()
print "Days with Errors over 1%"

for row in results:
    print "  ", row[0], " ", row[1], "%", "errors"

conn.close()
