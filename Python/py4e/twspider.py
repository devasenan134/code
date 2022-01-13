import twurl
import json
import ssl
import urllib.request

import sqlite3


twitterUrl = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect("spider.sqlite")
cur  = conn.cursor()

cur.execute("""
            CREATE TABE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTERGER)""")

    
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input("Enter a Twitter account, or quite: ")
    if acct == 'quit': break
   
    if len(acct) < 1:
        cur.execute("SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1")
        try:
            acct = cur.fetchone()[0]
        except:
            print("No unretrieved Twitter accounts found")
            continue

    
    url = twurl.augment(twitterUrl, {'screen_name': acct, "count": '5'})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url, context = ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)
#     print(json.dumps(js, indent=4))

    cur.execute("UPDATE Twitter SET  retrieved = 1 WHERE name = ?", (acct, ))

    countnew = 0
    countold = 0

    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute("SELECT friends FROM Twitter WHERE name = ?  LIMIT 1", (friend, ))

        try:
            count = cur.fetchone()[0]
            cur.execute("UPDATE Twitter SET friends = ? WHERE name = ?", (count+1, friend))
            countold = countold + 1

        except:
            cur.execute("""INSEERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)""", (friend, ))
            countnew = countnew + 1 


    print("New accounts=", countnew, "retrieved=", countold)
    conn.commit()
