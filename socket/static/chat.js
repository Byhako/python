var socket = io.connect('http://' + document.domain + ':' + location.port)
socket.on('connect', function () {
  console.log('hola')
  socket.emit('chat', {
    data: 'I\'m connected!'
  })
})


$(document).ready(function(){

  $('#send').click(function() {
    var name = $('#name').val().toUpperCase() 
    var message = $('#message').val()
    var mensaje = "<span id='user'>"+name+" : </span>"+message+"<br/>"
    socket.emit('send', mensaje)
  })

  socket.on('mensaje', function (data) {
    console.log(data)
    $('#display').append(data)
  })

})
