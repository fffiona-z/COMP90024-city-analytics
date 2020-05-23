function (doc) {
  var crime_related = ["violence","fraud","genocide","addict","crook","derelict","felon",
                       "hooker","hustler","junkie","miscreant","panhandler","suspect","thief","thugs","vandal",
                       "conspiring","defrauding","fearless","greedy", "horrific", "killing", "maiming",
                       "rampage", "senseless", "stalking", "terrorize", "threatening","Abuse", "Accessory",
                       "accomplice", "accused", "accuser", "activists", "adversary","affect", "afis","aggravated", "assault",
                        "alcohol", "arraignment", "arrest", "arsenal", "arson", "assailant", "assault", "attack", "autopsy",
                       "belligerence", "blackmail", "bloodstain", "bombing", "brawl", "break-in", "breaking and entering", "Bribery",
                       "Brutality", "Bullying", "Burglary", "Bystander","Cheat", "Civil", "Claim", "Coercion", "Collusion", "Combat",
                       "Commission", "Controversial", "Conviction", "Cops", "Coroner", "Corruption", "theft", "Crime", "Criminal","Criminology", "Cuffs", "Custody",
                       "Damage", "Danger", "Dangerous", "Dark side", "Deadly","Death","Deliberate", "Delinquency", "Detain","Dismember", "Disobedience",
                        "Disorderly", "Dispatch", "Disruption","drug","Elusive", "Embezzle", "Emergency", "Enable","Escape", "Evil","Extort", "Extradition",
                        "FBI", "Federal", "Felony", "Ferocity", "Fight", "fingerprint", "Firebombing", "flee", "Force", "Forensics", "Forgery",
                        "Fraud", "furtive","gun","gang","Holster","Illegal", "Immoral", "Immunity", "Impeach", "Incarceration", "Incompetent", "Incriminating",
                        "Indictment", "Injury", "Inmate", "Innocence", "Interrogate","Intruder", "Invasive", "Investigate","Jail","Jury","Juvenile","Kidnapping",
                        "Kill", "Killer", "Kin","Leaks", "Lease", "Libel", "Liberty","Lie" , "Lowlife","Mace", "Malpractice", "Manacled", "Manslaughter", "Marshal",
                        "Mayhem", "Metal", "Miscreant", "Misdemeanor", "Missing person", "money laundering", "Moratorium", "Motorist", "Murder",
                        "Nuisance","Obey", "Obligation", "Offender", "Offense","Pedestrian","Penalize", "Penalty", "Perjury","Probation","Prohibit","Quake","Quarrel",
                         "Radar", "Raid","Rape", "Refute", "Repeal", "Reported", "Resist","Restriction", "Revenge", "Riot", "Robbery", "Rogue", "Rough",
                         "Sabotage", "Safeguard", "Sanction", "Scene", "Serial killer", "Seriousness", "Shackles", "Sheriff", "Shooting", "Shyster",
                         "Slander", "Slashing", "Slaying", "Smuggling", "Sorrow", "Speculation", "Spying", "Squad", "Stabbing", "Stalking", "Statute",
                         "Statute of limitation", "Stigma", "Stipulation", "Subdue", "Subpoena","Surveillance", "Suspect", "Sworn", "Terrorism",
                         "Testify", "Testimony", "Theft", "Threatening", "Three-strikes law", "Thwart", "Tire-slashing", "Torture", "Tragedy",
                         "Trauma", "Trooper", "Understaffed","Unlawful", "Vagrancy", "Vandalism", "Viable", "Vice", "Victim", "Victimize",
                         "Violate", "Violation", "Violence","voyeurism", "Vulnerable", "Ward", "Warning", "Warped", "Warrant", "Weapon","Wiretap",
                          "zealot"];
  var cities = ["Darwin","Palmerston","Brisbane","Bundaberg" ,"Caboolture","Cairns","Caloundra","Gladstone","Gold Coast","Gympie","Hervey Bay","Ipswich"
               ,"Logan","Mackay", "Maryborough", "Mount Isa","Rockhampton","Sunshine Coast","Toowoomba","Townsville", "Adelaide", "Mount BarkerMount",
                "Gambier", "Murray Bridge", "Port Adelaide" ,"Port Augusta" ,"Port Pirie", "Port Lincoln", "Victor Harbor", "Whyalla","Hobart","Burnie",
                ,"Devonport","Launceston", "Melbourne","Ararat","Bairnsdale","Benalla","Ballarat","Bendigo","Dandenong","Frankston","Geelong","Hamilton",
                "Horsham", "Latrobe", "Melton","Mildura","Sale","Shepparton","Swan Hill","Wangaratta","Warrnambool","Wodonga","Perth", "Albany","Bunbury",
                "Busselton","Fremantle","Geraldton","Joondalup","Kalgoorlie","Karratha","Mandurah","Rockingham","Sydney","Albury","Armidale","Bathurst",
                "Blue Mountains","Broken Hill","Campbelltown","Cessnock","Dubbo","Goulburn","Grafton","Lithgow","Liverpool","Newcastle","Orange","Parramatta",
                "Penrith","Queanbeyan","Tamworth","Wagga","Wollongong"]
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
}
