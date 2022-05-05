function register() {
 
    var sUsername = document.getElementById("re_name");
    var sPass = document.getElementById("re_password");

    if (sUsername.value == "admin2" && sPass.value == "123456"){
        alert("注册成功！");
    }
    else{
        alert("注册失败，请检查输入!");
    }
        
}
function onClick(){
    window.location.href="../登录/登录页面.html";
}
