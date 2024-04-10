var SearchHandler = function (){}

SearchHandler.prototype.listenSubmitEvent = function (){
  $("#search").on("click", function (event){
    event.preventDefault();
    var content = $("input[name='content']").val();
    var position_name = $("a[id='position_name']").text();

    myajax.get({
      url: "/donglin/search/",
      data: {
       content,
        position_name
      },
      success: function (result){
        if(result['code'] == 200){
          var datas = result["datas"]
          console.log(datas)
        }else{

        }
      }
    })
  });
}

SearchHandler.prototype.run = function (){
  this.listenSubmitEvent();
}


$(function (){
  var handler = new SearchHandler();
  handler.run();
});