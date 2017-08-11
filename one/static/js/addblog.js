'use strict';
function isImg(){
  var title = document.getElementById('title').value;
  var content = document.getElementById('content').value;
  if (title != '' || content != '') {
    return True;
  }else{
    alert('输入不能为空!')
    return false;
  }
};
function startOne(obj){
  var value = obj.getAttribute('id');    //这里是获取其中属性
  window.location.href = 'http://192.168.0.202:8000/blog/oneblog/?title=' + value;
}
// KE.show({
//                 name: 'content',
//                 allowUpload: true,
//                 imageUploadJson: '/article/upload/kindeditor',
//         });
