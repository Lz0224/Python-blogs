
//这里不知道为什么不能使用jquery
function getList(obj){
  var value = obj.getAttribute('id');    //这里是获取其中属性
  window.location.href = 'http://192.168.0.202:8000/blog/oneblog/?title=' + value;
}
