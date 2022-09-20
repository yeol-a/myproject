// http 모듈
// 웹페이지의 요청과 응답에 관련된 모듈
// 웹 서버 생성

var http = require('http');
var server = http.createServer();

// listen(prot) : 서버를 실행 
server.listen(52222, function(){
    console.log("server running success")
});

// listen은 서버 대기 상태임. 

setTimeout(function(){
    server.close();
})
