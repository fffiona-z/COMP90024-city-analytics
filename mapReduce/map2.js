
    // author: Group25
    //         Fangfei Zheng 965378 (China)
    //         Jingjiahui Lu 966172 (Melb)
    //         Xi Chen 983241(China)
    //         Haoran Zhang 960374 (China)
    //         Pengnan Zhao 883338(China)
 

function (doc) {
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
}
