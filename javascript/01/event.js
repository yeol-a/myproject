process.on('exit', function() {
    console.log('종료합니다.')
})

process.on('uncaughtException', function(error) {
    console.log('예외발생')
})

var count = 0;
/* 이벤트를 주기적으로 받아와야하는 경우 사용하는 함수 */
var id = setInterval(function() {
    count+=1;
    /* clearInterval : 즉시 종료를 원할 경우 사용 */
    if (count==3) {clearInterval(id);}
    error.error.error();
});

// exit이라는 이벤트를 가져옴 (프로세스를 종료시킬 때)
// 종료합니다라는 동작을 일으키는 함수를 만듦

// 