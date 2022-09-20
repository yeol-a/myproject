// 예외처리는 try catch 구문 사용

var fs = require('fs');
try {
    var data = fs.readFileSync('txtfile.txt', 'utf-8');
    console.log(data);
} catch(e) {
    console.log(e)
}

// try 구문을 써서 파일을 입력
try {
    fs.writeFileSync('txtfile.txt', 'Hello', 'utf-8')
    console.log('file write complete')
} catch(e) {
    console.log(e)
}