// 서버 측에서 응답을 해주는 코드
// writeHead(statusCode, object)
// end([data], [encoding])

var http = require('http');
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
    // 응답코드
    response.writeHead(200, {'Content-Type':'text/html'});
    response.end('<h1>Hello</h1>')
}).listen(52222, function(){
    console.log("good")
})

