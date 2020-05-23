function (doc) {

  if(doc.text != null){
      if(doc.text.indexOf("covid") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("covid19") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("covid-19") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("COVID") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("COVID19") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("COVID-19") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("coronavirus") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("coronavirus19") != -1)
        emit(["COVID-19",doc.place.name],1);
      else if(doc.text.indexOf("coronavirus-19") != -1)
        emit(["COVID-19",doc.place.name],1);
  }
  else if(doc.tweet.text != null){
    if( doc.tweet.text.indexOf("covid") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("covid-19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("covid19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("COVID") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("COVID19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("COVID-19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("coronavirus") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("coronavirus19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
    else if( doc.tweet.text.indexOf("coronavirus-19") != -1)
       emit(["COVID-19",doc.tweet.place.name],1);
  }

}
