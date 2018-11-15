var data; 

/*This is client side javascript. 
It will listen for any click on notification link, prevent the default action,
send xhr async request to nodejs server asking it to scrape the data. On receiving the data,
store the data in local storage and change the page to target page which was supposed to happen on clicking the hyperlink.*/

var obj = {
    xhr: new XMLHttpRequest(),
    linkclick: function(e){
        e.preventDefault();
        var update = function(response){
            data = response;
            localStorage.setItem('Data_for_table', data);
            window.location.href= "test1.html";            
        }
        obj.getData(update);
    },
    
    getData: function(callback){
        this.xhr.onreadystatechange= function(){
            if(this.readyState==4 && this.status==200){
                var res=this.responseText;
                console.log(res);
                callback.apply(this, [res]);
            }
        };
        this.xhr.open("GET","http://localhost:7000",true);
        this.xhr.send();
        
    }
}
