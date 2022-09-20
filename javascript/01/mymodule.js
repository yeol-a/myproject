// exports 객체를 사용하면 다른 js 파일에서 불러서 사용 가능
// 절대값을 구하는 함수 

exports.abs = function (number) {
    if (number > 0) {
        return number;
    }
    else {
        return -number;
    }
}

// 원의 넓이를 구하는 함수 
exports.CircleArea = function (radius) {
    return radius * radius * 3.14 
}