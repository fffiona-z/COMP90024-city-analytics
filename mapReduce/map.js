function(doc){
    var lib =  require("mapReduce/lib");
    if(lib.hashtagFamily(doc.entities.hashtags) == "#COVID-19"){
       emit([lib.hashtagFamily(doc.entities.hashtags),doc.place.name],1);
    }
}