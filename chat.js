var net = require("net");

var chatServer = net.createServer();

function handleData(data){
	console.log(data);
}

function handleConnection(client){
	client.write("Hi!\n");

	client.on("data", handleData);
}

chatServer.on(connection, handleConnection);