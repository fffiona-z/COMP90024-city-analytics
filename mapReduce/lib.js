var families = {"#COVID-19": ["#covid", "#covid19", "#COVID", "#COVID19", "#COVID-19", "#coronavirus", "#coronavirus19","#covid-19","#coronavirus-19"]};
exports.hashtagFamily = function (hashtag) {
  var hashFamily = "other-topic";
  Object.getOwnPropertyNames(families).forEach(function (family) {
    if (families[family].indexOf(hashtag) >= 0) {
      hashFamily = family;
    }
  });
  return hashFamily;
};