var awsIot = require('aws-iot-device-sdk');

// config
var device = awsIot.device({
	keyPath: "5dad5a6669-private.pem.key",
	certPath: "5dad5a6669-certificate.pem.crt",
	caPath: "RootCA.crt",
	host: "a12052znnai1ys-ats.iot.us-east-1.amazonaws.com"
});

// connect
device.on('connect', function() {
				console.log('Connected');});

// error
device.on('error', function(error) { console.log('Error: ', error); });

// subscribe
device.subscribe("myTopic")

// publish to myTopic
device.publish("myTopic", JSON.stringify({
status: 'closed'
}));

// receive message from topics this device is subscribed to
device.on('message', function(topic, payload){
	console.log('message', topic, payload.toString()); process.exit();
});


