var http = require('http');
var scrape = require('./scraper.js');
const url = 'http://www.cbic.gov.in/Customs-Notifications';


var server = http.createServer(function(request, response){
    /*This function creates an http server which listens for connections from client and scrapes data.
	Once scraped data is available then it sends it back to the client in JSON format. 
	Client uses this JSON data to create table and populate it. */
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.setHeader('Access-Control-Request-Method', '*');
	response.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');
	response.setHeader('Access-Control-Allow-Headers', '*');
	if ( request.method === 'OPTIONS' ) {
		response.writeHead(200);
		response.end();
		return;
    }
    else{
        scrape.scrape_data(url).then(function(x){
            var obj = {data: x};
            response.writeHead(200, {'Content-type':'text/plain'});
            response.write(JSON.stringify(obj));
            response.end();
        })
    }
});
console.log("Server listening at 7000");
server.listen(7000);