var LoginHandler = function (){}

LoginHandler.prototype.listenSubmitEvent = function (){
  $("#login").on("click", function (event){
    event.preventDefault();
    var email = $("input[name='username_login']").val();
    var password = $("input[name='password_login']").val();

    myajax.post({
      url: "/donglin/login/",
      data: {
        "email":email,
        "password":password,
      },
      success: function (result){
        if(result['code'] == 200){
          window.location = "/"
        }else{
          console.log("")
          alert(result["message"]);
        }
      }
    })
  });
}

LoginHandler.prototype.run = function (){
  this.listenSubmitEvent();
}


$(function (){
  var handler = new LoginHandler();
  handler.run();
});