// 배열
// 자바스크립트에서의 배열은 다른 객체와는 다른 취급을 받음
// 일반적인 객체는 '속성 : 속성값' 으로 이루어져 있음
// 배열 객체는 '요소 : 항목' 이라고 부름
// 객체와 마찬가지로 배열 안에 여러 개의 값을 저장 가능
// 자바스크립트에서의 '배열 객체' = 파이썬의 '리스트' (순서가 존재하기 때문)
// 인덱스를 통해 값에 접근

const arr = ['one', 'two', 'three']
console.log(arr[0]);
console.log(arr[1]);

// 배열에 값 추가
arr.push("four");
console.log(arr);

// 배열에 요소 제거
arr.splice(3,1);
console.log(arr);

arr.pop();
console.log(arr);