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

tweets = []
aurins = []

@app.route('/')
def home():
    return render_template('home.html')

# communicate to the CouchDB and return the results
@app.route('/city_analysis/service', methods=['GET'])
def service():
    tweets = []
    search_from_db("tweet")
    if len(aurins) == 0:
        search_from_db("aurin")
    return render_template('home.html', tweet=simplejson.dumps(tweets), aurin=simplejson.dumps(aurins))

def search_from_db(view):
    if view == "aurin":
        for row in aurin_counts_view(g.couch):
            keys = row.keys()
            aurins.append(dict(keys[1], row.value))
    elif view == "tweet":
        for row in tweet_counts_view(g.couch):
            keys = row.keys()
            tweets.append(dict(keys[1], row.value))



if __name__ == '__main__':
    app.config.update(
        DEBUG = True,
        COUCHDB_SERVER = 'http://admin:12345@localhost:5984/',
        COUCHDB_DATABASE = 'tweet4'
    )
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    manager.add_viewdef([tweet_counts_view, aurin_counts_view])
    manager.sync(app)
    app.run(host='0.0.0.0', port=5000, debug=True)