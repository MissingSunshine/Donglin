var RegisterHandler = function (){

}


RegisterHandler.prototype.listenSubmitEvent = function (){
  $("#register").on("click", function (event){
    event.preventDefault();
    var email = $("input[name='email_register']").val();
    var username = $("input[name='username_register']").val();
    var password = $("input[name='password_register']").val();

    myajax.post({
      url: "/donglin/register/",
      data: {
        "email": email,
        "username": username,
        password, // "password": password
      },
      success: function (result){
        if(result['code'] == 200){
          window.location = "/";
        }else{
          alert("失败");
        }
      }
    })
  });
}

RegisterHandler.prototype.run = function (){
  this.listenSubmitEvent();
}

// $(function(){})
$(function (){
  var handler = new RegisterHandler();
  handler.run();
})
