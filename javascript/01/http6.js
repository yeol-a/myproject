var http = require('http');
var fs = require('fs');


require('http').createServer(function(request, response){
    if (request.method == "GET") {
        fs.readFile('label.html', function(error, data){ // label.html이 제출된다면, 추가동작은 function을 따름~이건 폼태그 덕분에 가능 
            response.writeHead(200, {'Content-Type':'text/html'});
            response.end(data)
        });
}
    else if (request.method == 'POST'){
    request.on('data', function(data){
        response.writeHead(200, {'Content-Type':'text/html'});
        response.end('<h1>'+data+'</h1>')
    })
    }
}).listen(52222, function(){
    console.log("good")
});

// request.on 페이지 양식을 보여줌
// html의 form과 연결이되는 지점이 function
// 앞의 데이터는 홈페이지가 나오는 거 / 뒤의 data는 넘겨줄 거 

// 대부분의 홈페이지는 post 방식. 
// post로 요청이 들어오면, 홈페이지 띄워주고, 거기서 일어난 동작들에서, 데이터를 받아서, 그 데이터를 넣어서 제목1로 지정해서 보여주세요
// 이것은 추후에 배우게 될 장고와 연동이 되는 것임
// javascript는 프론트와 백엔드 다 가능한 언어! 프론트에서 받은 것을 html의 폼태그를 통해서 백엔드로 넘겨서 백엔드 상에서 일어나는 일은 
// 이제 장고에게 주는 것임~



