var http = require('http');
var fs = require('fs');
var server = http.createServer();

// 서버 이벤트를 연결
server.on('request', function(){
    console.log("Request On")
});

server.on('connection', function(){
    console.log('connection');
});

server.on('close', function(){
    console.log('close');
});

server.listen(8811, () => {
    console.log("hi this is my server")
})

require('http').createServer(function(request, response){
    response.writeHead(404, {'Content-Type':'text/html'});
    response.end()
    })
.listen(52222, function(){
    console.log("good")
})
