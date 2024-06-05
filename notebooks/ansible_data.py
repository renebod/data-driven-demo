import couchdb
import pandas as pd


def getdb(dbname):
    user = "admin"
    password = "password"
    couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))
    if dbname in couchserver:
        db = couchserver[dbname]
    else:
        # del couchserver[dbname]
        db = couchserver.create(dbname)
    return db


def listdocs():
    rows = getdb('mydb').view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    df = df.drop(columns="_id")
    df = df.drop(columns="_rev")
    return df


def newdoc():
    doc_type = input("Please enter a document type ")
    new_doc = {}
    new_doc['doc_type'] = doc_type
    while True:
        add = input("Do you want to add another field? (y/n) ")
        if add == 'n':
            break
        key = input("What field would you like to add? ")
        value = input("What value would you like to add? ")
        new_doc[key] = value
    getdb('mydb').update([new_doc])
    return listdocs()