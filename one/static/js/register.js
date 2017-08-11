'use strict';
function isNull(){
  var age = document.getElementById('age').value;
  var email = document.getElementById('email').value;
  var name = document.getElementById('username').value;
  var pwd = document.getElementById('password').value;
  if (name != '' || pwd != '' || email != '' || age != 0) {
    return True;
  }else{
    alert('输入不能为空!')
    return false;
  }
};

function showerror(str){
  var xmlhttp;
  alert(str)
  if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
  }else {
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
  }
  xmlhttp.onreadystatechange = function(){
    if (xmlhttp.readyState == 4 && xmlhttp.state == 400) {
      document.getElementById('lname').innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open('GET', '/ajax/gethint.asp?q=' + str, true);
  xmlhttp.send();
}
