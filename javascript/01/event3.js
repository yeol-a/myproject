process.on('exit', function(){
    console.log('bye');
})

// 프로세스 종료
process.exit();

// 이벤트 강제 발생 (이게 비동기?)
process.emit('exit');
process.emit('exit');
process.emit('exit');
process.emit('exit');


