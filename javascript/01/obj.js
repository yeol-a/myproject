// 자바스크립트에는 전역 객체도 존재
// console : 콘솔 화면과 관련된 기능을 다루는 객체
// console에 존재하는 메서드
// log() : 출력
// 특수문자 : %d(정수), %s(문자열). %j(JSON)-> 속성값, 설정값 등 

console.log('output: %d', 0920);

//%d가 넘쳐났을 때 어떻게 처리되는가? => 부족한 부분을 다 채워서 출력이 됨 
console.log('%d + %d = %d', 273, 27, 273+27);
console.log('%d + %d = %d', 273, 27, 273+27, 63368);
console.log('%d + %d = %d & %d', 273, 27, 273+27);

// process : 프로그램을 다루는 객체
// argv : 실행 매개 변수
// env : 환경 변수
// version : node.js 버전
// exit() : 프로그램 종료 
console.log('process env', process.env);
console.log('process version', process.version);
process.exit();


// exports 객체
// 모듈과 관련 - 모듈 : 메서드와 속성을 미리 정의해놓은 것  
// 객체(클래스) = 모듈 

