// os 모듈
// 운영체제와 관련된 모듈
// require로 추출해야 함
// hostname(): 운영체제 호스트 네임을 전달
// type() : 운영체체의 이름
// arch() : 시스템 아키텍쳐 (32, 64bit 등등)

var os = require("os");
console.log(os.hostname());
console.log(os.type());
console.log(os.arch());

// url 모듈
// url 부분 추출
// parse() : URL 문자열을 URL 객체로 전달 
// formnat() : URL 객체를 URL 문자열로

// Query String 모듈
// 쿼리는 요청을 하는 것
// stringfy() : 쿼리 객체를 쿼리 문자열로 변환
// parse() : 쿼리 문자열을 쿼리 객체로 변환 
// https://hangul.co.kr/book/book.html?isbn=
// 물음표 이후 부분을 '쿼리'라고 함 (추가적인 요청)


var url = require('url');
var parseObject = url.parse('https://hangul.co.kr/book/book.html')
console.log(parseObject)

var url2 = require('url');
var querystring=require('querystring');

var parseObject = url.parse('https://hangul.co.kr/book/book.html?isbn=...')
console.log(querystring.parse(parseObject.query))

// 쿼리는 URL과 한 몸?

// util 모듈
// 문자열 추출하는데 쓰임
// format() : 매개변수로 입력한 문자를 조합해서 변환 (format은 문자열을 엮는 역할)
var util=require('util')
var data=util.format('%d + %d = %d', 273, 27, 273+27);
console.log(data)

// FileSystem 모듈
// 파일 처리와 관련된 모듈 
// readFile(file, encoding, callback) 비동기  
// readFile(file, encoding) 동기식
// writeFile(file, encoding, callback) 비동기
// writeFile(file, encoding) 동기식 
var fs = require('fs')
var text = fs.readFileSync('textfile.txt', 'utf-8')
console.log(text)

// 예외처리

