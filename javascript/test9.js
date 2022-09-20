// 객체(클래스)에서 정의된 함수를 '메소드'라고 부름 
// increaseX : function () => 속성 : 속성값 

const obj = {
    x : 0,
    increaseX : function() {
        this.x = this.x+1;
    }
}

// this는 화살표함수 x를 가져오기 위해 this.x로 호출했다 (새롭게 x를 assign 해주는 것이 아니라)

console.log(obj)
console.log(obj.x)
console.log(obj.increaseX())
obj.increaseX()
console.log(obj.x)
