

/*This is client side javascript. 
It will listen for any click on notification link prevent the default action, 
send xhr async request to nodejs server asking to scrape the data and then on receiving the data,
store the data in localstorage and change the page to another page which was supposed to happen on clicking the hyperlink.*/

var obj = {
    xhr: new XMLHttpRequest(),
    linkclick: function(e){
        e.preventDefault();
        var update = function(response){
            location.href= "#Notifications";   
            obj.load(response);
        }
        obj.getData(update);
    },
    load: function(res){
        console.log(res);
        var data = JSON.parse(res);
        var complete_data = data.data;
        var table = this.buildPopulatedTable(complete_data);
       // console.log(table);
        document.body.appendChild(table);
    },
    buildPopulatedTable: function(complete_data){
        var headers = ["Notification No. and Date of Issue", "PDF", "Subject"];

        table = document.createElement("table");
        var table_body = document.createElement("tbody");
        table.setAttribute("class", "border_class");

        var header_row = document.createElement("tr");
        header_row.setAttribute("class", "header_class");

        for(var i = 0; i < headers.length; i++){
            var td = document.createElement("td");
            td.appendChild(document.createTextNode(headers[i]));
            header_row.appendChild(td);
        }
        table_body.appendChild(header_row); 
        for(var i = 0;i < 8 ;i++){ 
            var tr = document.createElement("tr");
            tr.setAttribute("class", "tr_class");

            var td1 = document.createElement("td");
            td1.appendChild(document.createTextNode(complete_data[i][0]));
            var td2 = document.createElement("td");
            var link_to_pdf = document.createElement("a");
            link_to_pdf.href = "http://www.cbic.gov.in"+ complete_data[i][1];
            link_to_pdf.innerHTML = "View";
            td2.appendChild(link_to_pdf);
            var td3 = document.createElement("td");
            td3.appendChild(document.createTextNode(complete_data[i][2]));
            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);
            table_body.appendChild(tr);
        }
        table.appendChild(table_body);
        return table;
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
