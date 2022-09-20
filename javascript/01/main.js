// let: 변하는 변수 
// const: 변하지 않는 변수
// var: 두리뭉실한 변수
// 메모리를 효율적으로 활용하기 위해서, let과 const가 탄생한 것

var mymodule = require('./mymodule.js');
console.log('abs(-273) = %d' , mymodule.abs(-273));
console.log('CircleArea = %d' , mymodule.CircleArea(3));

//.js 파일을 파이썬에서 모듈로 불러오듯이 불러올 수 있음
// 불러오기 위해서는 require 함수를 사용해야 

