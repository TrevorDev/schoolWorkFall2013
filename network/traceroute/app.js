traceroute = require('traceroute');

countHops = function(hops){
	counter = 0;
	for(var i = 0;i<hops.length;i++){
		if(hops[i]!=false){
			counter++;
		}
	}
	return counter;
}
biggest = 0;
traceNow = function(domain){
	traceroute.trace(domain, function (err,hops) {
	  if (!err) {
	  	var num = countHops(hops);
	  	if(num>biggest){
	  		console.log(hops);
	  		biggest=num;
	  		console.log(num+" "+domain);
	  	}
	  }else{
	  	//console.log("error");
	  }
	});
}




var fs = require('fs'),
    readline = require('readline');

var rd = readline.createInterface({
    input: fs.createReadStream('sites.txt'),
    output: process.stdout,
    terminal: false
});

rd.on('line', function(line) {
    //console.log(line);
    //traceNow(line);
});

traceNow('cctv.com');
//console.log("hit");