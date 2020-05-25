from flask import Flask, render_template, abort, url_for, g, jsonify
from couchdb.design import ViewDefinition
import flaskext.couchdb
from all_city import all_city
import simplejson
from copy import deepcopy

app = Flask(__name__)

# create CouchDB views
tweet_counts_view = ViewDefinition('crime','tags_city_counts', '''\
    function (doc) {
        var crime_related = ["violence", "fraud", "genocide",\
            "addict", "crook", "derelict", "felon", "hooker",\
            "hustler", "junkie", "miscreant", "panhandler",\
            "suspect", "thief", "thugs", "vandal", "conspiring",\
            "defrauding", "fearless", "greedy", "horrific", "killing",\
            "maiming", "rampage", "senseless", "stalking", "terrorize",\
            "threatening", "Abuse", "Accessory", "accomplice", "accused",\
            "accuser", "activists", "adversary", "affect", "afis",\
            "aggravated", "assault", "alcohol", "arraignment", "arrest",\
            "arsenal", "arson", "assailant", "assault", "attack", "autopsy",\
            "belligerence", "blackmail", "bloodstain", "bombing", "brawl",\
            "break-in", "breaking and entering", "Bribery", "Brutality",\
            "Bullying", "Burglary", "Bystander","Cheat", "Civil", "Claim",\
            "Coercion", "Collusion", "Combat", "Commission", "Controversial",\
            "Conviction", "Cops", "Coroner", "Corruption", "theft", "Crime",\
            "Criminal", "Criminology", "Cuffs", "Custody", "Damage",\
            "Danger", "Dangerous", "Dark side", "Deadly", "Death",\
            "Deliberate", "Delinquency", "Detain", "Dismember",\
            "Disobedience", "Disorderly", "Dispatch", "Disruption", "drug",\
            "Elusive", "Embezzle", "Emergency", "Enable", "Escape", "Evil",\
            "Extort", "Extradition", "FBI", "Federal", "Felony", "Ferocity",\
            "Fight", "fingerprint", "Firebombing", "flee", "Force",\
            "Forensics", "Forgery", "Fraud", "furtive", "gun", "gang",\
            "Holster", "Illegal", "Immoral", "Immunity", "Impeach",\
            "Incarceration", "Incompetent", "Incriminating", "Indictment",\
            "Injury", "Inmate", "Innocence", "Interrogate", "Intruder",\
            "Invasive", "Investigate", "Jail", "Jury", "Juvenile",\
            "Kidnapping", "Kill", "Killer", "Kin", "Leaks", "Lease", "Libel",\
            "Liberty", "Lie", "Lowlife", "Mace", "Malpractice", "Manacled",\
            "Manslaughter", "Marshal", "Mayhem", "Metal", "Miscreant",\
            "Misdemeanor", "Missing person", "money laundering",\
            "Moratorium", "Motorist", "Murder", "Nuisance","Obey",\
            "Obligation", "Offender", "Offense", "Pedestrian", "Penalize",\
            "Penalty", "Perjury", "Probation", "Prohibit", "Quake", "Quarrel",\
            "Radar", "Raid", "Rape", "Refute", "Repeal", "Reported", "Resist","Restriction", "Revenge", "Riot", "Robbery", "Rogue", "Rough",\
            "Sabotage", "Safeguard", "Sanction", "Scene", "Serial killer",\
            "Seriousness", "Shackles", "Sheriff", "Shooting", "Shyster",\
            "Slander", "Slashing", "Slaying", "Smuggling", "Sorrow",\
            "Speculation", "Spying", "Squad", "Stabbing", "Stalking",\
            "Statute", "Statute of limitation", "Stigma", "Stipulation",\
            "Subdue", "Subpoena", "Surveillance", "Suspect", "Sworn",\
            "Terrorism", "Testify", "Testimony", "Theft", "Threatening",\
            "Three-strikes law", "Thwart", "Tire-slashing", "Torture",\
            "Tragedy", "Trauma", "Trooper", "Understaffed", "Unlawful",\
            "Vagrancy", "Vandalism", "Viable", "Vice", "Victim",\
            "Victimize", "Violate", "Violation", "Violence", "voyeurism",\
            "Vulnerable", "Ward", "Warning", "Warped", "Warrant",\
            "Weapon", "Wiretap", "zealot"];
        var cities = ["Darwin", "Palmerston", "Brisbane", "Bundaberg",\
            "Caboolture", "Cairns", "Caloundra", "Gladstone", "Gold Coast",\
            "Gympie", "Hervey Bay", "Ipswich", "Logan", "Mackay",\
            "Maryborough", "Mount Isa", "Rockhampton", "Sunshine Coast",\
            "Toowoomba", "Townsville", "Adelaide", "Mount BarkerMount",\
            "Gambier", "Murray Bridge", "Port Adelaide", "Port Augusta",\
            "Port Pirie", "Port Lincoln", "Victor Harbor", "Whyalla",\
            "Hobart", "Burnie", "Devonport", "Launceston", "Melbourne",\
            "Ararat", "Bairnsdale", "Benalla", "Ballarat", "Bendigo",\
            "Dandenong", "Frankston", "Geelong", "Hamilton", "Horsham",\
            "Latrobe", "Melton", "Mildura", "Sale", "Shepparton",\
            "Swan Hill", "Wangaratta", "Warrnambool", "Wodonga", "Perth",\
            "Albany", "Bunbury", "Busselton", "Fremantle", "Geraldton",\
            "Joondalup", "Kalgoorlie", "Karratha", "Mandurah", "Rockingham",\
            "Sydney", "Albury", "Armidale", "Bathurst", "Blue Mountains",\
            "Broken Hill", "Campbelltown", "Cessnock", "Dubbo", "Goulburn",\
            "Grafton", "Lithgow", "Liverpool", "Newcastle", "Orange",\
            "Parramatta", "Penrith", "Queanbeyan", "Tamworth", "Wagga",\
            "Wollongong"];
        var check = 0;
        if(doc.text != null){
            for(var i = 0; i < crime_related.length; i++){
                if(doc.text.toLowerCase().indexOf(crime_related[i].toLowerCase()) != -1){
                    for(var j = 0; j < cities.length; j++){
                        if(doc.place.name == cities[j])
                            check = 1;
                    }
                }
            }

            if(check == 1)
                emit(["Topic related to crime",doc.place.name],1);
            check = 0;
        }
        else if(doc.tweet.text != null){
            for(var i = 0; i < crime_related.length; i++){
                if( doc.tweet.text.toLowerCase().indexOf(crime_related[i].toLowerCase()) != -1){
                    for(var j = 0; j < cities.length; j++){
                        if(doc.tweet.place.name == cities[j])
                            check = 1;
                    }
                }    
            }
        
            if(check == 1)
                emit(["Topic related to crime",doc.tweet.place.name],1);
            check = 0;
        }
    }''', '''\
    function(keys, values, rereduce) {
        if (rereduce) {
            return sum(values);
        } else {
            return values.length;
        }
    }''', group=True)


tweet_total_view = ViewDefinition('total_number', 'total_city_counts', '''\
    function (doc) {
        var cities = ["Darwin", "Palmerston", "Brisbane", "Bundaberg",\
            "Caboolture", "Cairns", "Caloundra", "Gladstone", "Gold Coast",\
            "Gympie", "Hervey Bay", "Ipswich", "Logan", "Mackay",\
            "Maryborough", "Mount Isa", "Rockhampton", "Sunshine Coast",\
            "Toowoomba", "Townsville", "Adelaide", "Mount BarkerMount",\
            "Gambier", "Murray Bridge", "Port Adelaide", "Port Augusta",\
            "Port Pirie", "Port Lincoln", "Victor Harbor", "Whyalla",\
            "Hobart", "Burnie", "Devonport", "Launceston", "Melbourne",\
            "Ararat", "Bairnsdale", "Benalla", "Ballarat", "Bendigo",\
            "Dandenong", "Frankston", "Geelong", "Hamilton", "Horsham",\
            "Latrobe", "Melton", "Mildura", "Sale", "Shepparton",\
            "Swan Hill", "Wangaratta", "Warrnambool", "Wodonga", "Perth",\
            "Albany", "Bunbury", "Busselton", "Fremantle", "Geraldton",\
            "Joondalup", "Kalgoorlie", "Karratha", "Mandurah", "Rockingham",\
            "Sydney", "Albury", "Armidale", "Bathurst", "Blue Mountains",\
            "Broken Hill", "Campbelltown", "Cessnock", "Dubbo", "Goulburn",\
            "Grafton", "Lithgow", "Liverpool", "Newcastle", "Orange",\
            "Parramatta", "Penrith", "Queanbeyan", "Tamworth", "Wagga",\
            "Wollongong"];
        var check = 0;
        if(doc.text != null){
            for(var j = 0; j < cities.length; j++){
                if(doc.place.name == cities[j])
                    check = 1;
            }

            if(check == 1)
                emit(doc.place.name,1);
            check = 0;
        }
        else if(doc.tweet.text != null){
            for(var j = 0; j < cities.length; j++){
                if(doc.tweet.place.name == cities[j])
                    check = 1;
            }

            if(check == 1)
                emit(doc.tweet.place.name,1);
            check = 0;
        }
    }''', '''\
    function(keys, values, rereduce) {
        if (rereduce) {
            return sum(values);
        } else {
            return values.length;
        }
    }''', group=True)

# @app.errorhandler(400)
# def not_found(error):
#     return render_template('400.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/')
def home():
    return render_template('home.html')

# communicate to the CouchDB and return the results
@app.route('/city_analysis/service', methods=['GET'])
def service():
    unemploy = deepcopy(all_city)
    population = deepcopy(all_city)
    search_unemploy(unemploy)
    search_popluation(population)
    tweets = deepcopy(all_city)
    for row in tweet_counts_view(g.couch):
        key = row.key[1]
        for tweet in tweets:
            if tweet.has_key(key):
                tweet[key] = row.value
    
    tweet_num = deepcopy(all_city)
    for row in tweet_total_view(g.couch):
        for tweet in tweet_num:
            if tweet.has_key(row.key):
                tweet[row.key] = row.value     
    
    data = { 'tweet' : simplejson.dumps(tweets),\
        'aurin' : simplejson.dumps(unemploy),\
        'population' : simplejson.dumps(population),\
        'tweet_num' : simplejson.dumps(tweet_num) }
    
    return data


def search_unemploy(unemploy):
    try:
        doc = g.couch['0000']
        if doc != None:
            features = doc['features']
            for feature in features:
                city_name = feature['properties']['lga_name']
                percent = feature['properties']['unemploymnt_3_percent']
                index = city_name.find('(') - 1
                city_name = city_name[:index]
                for item in unemploy:
                    if item.has_key(city_name):
                        item[city_name] = percent
                        break
    except:
        abort(404)

def search_popluation(population):
    try:
        doc = g.couch['1111']
        if doc != None:
            data = doc['data']
            for item in data:
                city_name = item['asciiname']
                total_num = item['population']
                for item in population:
                    if item.has_key(city_name):
                        item[city_name] = total_num
                        break
    except:
        abort(404)

if __name__ == '__main__':
    app.config.update(
        DEBUG = False,
        COUCHDB_SERVER = 'http://admin:12345@localhost:5984/',
        COUCHDB_DATABASE = 'tweet4'
    )
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    manager.add_viewdef((tweet_counts_view, tweet_total_view))
    manager.sync(app)
    app.run(host='0.0.0.0', port=5000, debug=False)
