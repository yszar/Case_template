var illegal_behavior = [
  [
    '进货时未查验许可证和相关证明文件',
    '安排未取得健康证明的人员从事接触直接入口食品的工作',
    '使用未经洗净消毒的餐具饮具和盛放直接入口食品的容器',
    '超过食品安全标准限量的',
    '未按要求进行食品贮存'
  ],
  ['南京', '苏州', '南通', '常州'],
  ['福州', '福安', '龙岩', '南平'],
  ['广州', '潮阳', '潮州', '澄海']
];

function get_illegal_behavior() {
  //获得省份下拉框的对象
  var sltCategory = document.illegal_behavior.category;
  //获得城市下拉框的对象
  var sltIllegal_behavior = document.illegal_behavior.illegal_behavior;
  //得到对应省份的城市数组
  var Category_I_B = illegal_behavior[sltCategory.selectedIndex - 1];

  //清空城市下拉框，仅留提示选项
  sltIllegal_behavior.length = 1;

  //将城市数组中的值填充到城市下拉框中
  for (var i = 0; i < Category_I_B.length; i++) {
    sltIllegal_behavior[i + 1] = new Option(Category_I_B[i], Category_I_B[i]);
  }
}
