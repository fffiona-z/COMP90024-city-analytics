from flask import Flask, render_template, redirect, url_for, g
from couchdb.design import ViewDefinition
import flaskext.couchdb
import simplejson

app = Flask(__name__)

# create CouchDB views

tweet_counts_view = ViewDefinition('tweet4','tags_city_counts', '''\
    function(doc){
        var lib = require("mapReduce/lib");
        if(lib.hashtagFamily(doc.entities.hashtags) == "#COVID-19"){
            emit([lib.hashtagFamily(doc.entities.hashtags),doc.place.name],1);
        }
    }''', '''\
    function(keys, values, rereduce){
        return sum(values);
    }''', group=True)

aurin_counts_view = ViewDefinition('aurin_data','tags_city_counts', '''\
    function(doc){
        var lib = require("mapReduce/lib");
        if(lib.hashtagFamily(doc.entities.hashtags) == "#COVID-19"){
            emit([lib.hashtagFamily(doc.entities.hashtags),doc.place.name],1);
        }
    }''', '''\
    function(keys, values, rereduce){
        return sum(values);
    }''', group=True)

results = []
aurin = []

@app.route('/')
def home():
    return render_template('home.html')

# communicate to the CouchDB and return the results
@app.route('/service/<city_name>', methods=['GET'])
def service(city_name):
    results = []
    search_from_db("tweet")
    tweet_data = search(city_name, results)
    if len(aurin) == 0:
        aurin_data = search(city_name, aurin)
    data = []
    data.append(tweet_data)
    data.append(aurin_data)
    return render_template('home.html', data=simplejson.dumps(data))

def search_from_db(view):
    if view == "aurin":
        for row in aurin_counts_view(g.couch):
            keys = row.keys()
            aurin.append(dict(keys[1], row.value))
    elif view == "tweet":
        for row in tweet_counts_view(g.couch):
            keys = row.keys()
            results.append(dict(keys[1], row.value))
    

def search(city_name, search_list):
    for item in search_list:
        if item.key == city_name:
            return item

if __name__ == '__main__':
    app.config.update(
        DEBUG = True,
        COUCHDB_SERVER = 'http://admin:12345@localhost:5984/',
        COUCHDB_DATABASE = ['tweet4', 'aurin_data']
    )
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    manager.add_viewdef([tweet_counts_view, aurin_counts_view])
    manager.sync(app)
    app.run(host='0.0.0.0', port=5000, DEBUG=True)