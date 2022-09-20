var custom = new process.EventEmitter();

custom.on('tick', function(){
    console.log("직접 만든 이벤트")
})

custom.emit('tick');
