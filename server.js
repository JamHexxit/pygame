const { Server } = require('ws');
 
const wss = new Server({ port: 25505 });
const connections = new Map();
let id = 1
wss.on('connection', (ws) => {
    message={
        type:"setup",
        info:{
            id:id,
        }
    }
    ws.send(JSON.stringify(message))
    id = ++id;
    ws.on('message', (data) => {
        const message = JSON.parse(data);
        if (message.type == "info") {
            connections.set(message.id,{ws:ws,name:message.info.name,x:0,y:0})
            console.log(message.id +" "+ message.info.name + " has connected")
        }
    })
});