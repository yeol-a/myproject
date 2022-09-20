// 객체

// 메모리에 저장된다는 점은 객체가 파이썬과 자바스크립트가 같음
// 파이썬에서 '클래스'라고 부르는 객체들의 집합 
// 자바스크립트에서는 파이썬의 클래스와 비슷하게 여러 값을 한 번에 담아 사용할 수 있는 자료구조가 존재 => '객체' 

// 객체를 사용할 때는 '속성 이름'과 '속성 값'을 사용함

const obj = {
    x : 0,
    y : 1
}

// 파이썬에서 class obj를 만들어서, 거기서 x=0, y=0 이라고 선언해준 것과 같음


// 객체의 속성 불러오기
console.log(obj.x);
console.log(obj['y']);

// 객체의 속성 변경하기
console.log(obj.x = obj.x + 1);
console.log(obj.x);

// 객체의 속성 제거 가능
delete obj.x 
console.log(obj.x)