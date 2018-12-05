var city = [
  ["北京", "天津", "上海", "重庆"],
  ["南京", "苏州", "南通", "常州"],
  ["福州", "福安", "龙岩", "南平"],
  ["广州", "潮阳", "潮州", "澄海"]
];

function getCity() {
  //获得省份下拉框的对象
  var sltProvince = document.test.status;
  //获得城市下拉框的对象
  var sltCity = document.test.status1;
  //得到对应省份的城市数组
  var provinceCity = city[sltProvince.selectedIndex - 1];

  //清空城市下拉框，仅留提示选项
  sltCity.length = 1;

  //将城市数组中的值填充到城市下拉框中
  for (var i = 0; i < provinceCity.length; i++) {
    sltCity[i + 1] = new Option(provinceCity[i], provinceCity[i]);
  }
}