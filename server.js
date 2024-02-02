const express = require('express');
const app = express();
const server = require('http').Server(app)

const { v4: uuidV4 } = require('uuid')

const io = require('socket.io')(server);

app.set('view engine', 'ejs')
app.use(express.static('public'));


app.get('/', (req, res) => {
    res.redirect(`/${uuidV4()}`)
})

app.get('/home', (req, res) => {
    res.render('index')
})


// app.get('/:room', (req, res) => {
//     res.render('room', { roomId: req.params.room })
// })

// io.on('connection', socket => {
//     console.log('Connected')
//     socket.on('join-room', (roomId, userId) => {
//         socket.join(roomId)
//         socket.to(roomId).emit('user-connected', userId)


//         socket.on('disconnect', () => {
//             socket.to(roomId).emit('user-disconnected', userId)
//         })
//     })


// })

io.on('connection', (socket) => {
    console.log('A user connected with socket : ', socket.id);

    // Handle message event

    socket.on('user-drawing', data => {
        console.log(data)
        console.log('User is drawing')
        socket.broadcast.emit('user-drawing', data)
    })

    socket.on('initialising', data => {
        socket.broadcast.emit('initialising', data)
    })


    socket.on('user-not-drawing', () => {
        socket.broadcast.emit('user-not-drawing')
    })

    socket.on('change-color', (color) => {
        socket.broadcast.emit('change-color', color)
    })

    // Handle disconnect event
    socket.on('disconnect', () => {
        console.log('A user disconnected');
    });
});


server.listen(3000, () => {
    console.log('running on port 3000')
})