function login() {
 
    var sUsername = document.getElementById("username");
    var sPass = document.getElementById("password");
 
    if (sUsername.value == "") {
 
        alert("请输入用户名");
 
    } else if (sPass.value  == "") {
 
        alert("请输入密码");
 
    } else if(sUsername.value == "admin" && sPass.value == "123456"){
 
        window.location.href="../首页/首页页面.html";
 
    } else {
 
        alert("请输入正确的用户名和密码！")
 
    }
}

function onClick(){
    window.location.href="../注册/注册.html";
}