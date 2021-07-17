var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var request = new XMLHttpRequest()

request.open('GET','https:api.github.com/users/megha1823/repos',true)

request.onload = function(){
    var data = JSON.parse(this.response);
    console.log(data);
}

request.send();