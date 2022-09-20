// http 모듈
// 웹페이지의 요청과 응답에 관련된 모듈
// 웹 서버 생성

const { copyFileSync } = require('fs');
var http = require('http');
var server = http.createServer();

// 서버 이벤트를 연결
server.on('request', function(){
    console.log("Request On")
});

server.on('connection', function(){
    console.log('connection');
});

// listen(port) : 서버를 대기시킴
server.listen(5001);

// request : 클라이언트가 요청할 때 발생하는 이벤트
// connection : 클라이언트가 접속할 때 발생하는 이벤트
// close : 서버가 종료될 때 발생하는 이벤트
// checkContinue : 지속적인 연결을 하고 있을 때 발생하는 이벤트
