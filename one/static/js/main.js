
    function login(){
       window.location.href="http://192.168.0.107:8000/users/login/";
    }
    function start(){
      var width = document.body.clientWidth
      var height = document.body.clientHeight
      var myvideo = document.getElementById('mainvideo');
      myvideo.width = width;
      myvideo.height = height;
      setTimeout('login()', 87000)

    }
    window.onload = start;
