var empTask= new Object();
var emp;
var sendCon = new Object();
//when document loads

function onLoad()
{
    console.log("really?");
    var divDoc = document.getElementById("writeContent");
    divDoc.style.visibility = 'hidden';
}

// when either user is selected or task is selected for assigning
function quotation(ele)
{
    sendCon.name = $(ele).parent().siblings(":first").text()
    console.log("hahaha");
    document.getElementById("writeQuotation").value = '';
    document.getElementById("writeContent").style.visibility = "visible";
}

function ente(ele)
{
    console.log("lolol");
}

function quot(ele)
{
    console.log("Inside quot")
    var data = new Object();
    data.type = $(ele).parent().prev().prev().prev().text();
    data.time = $(ele).parent().prev().children(":first").val();
    console.log(data.type);
    console.log(data.time);
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/quot',
        success: function (data) 
        {
            console.log("Inside success")
            //document.getElementById("reg_val").innerHTML=data.responseText
            /*
            response = JSON.parse(data)
            document.getElementById("reg_val").innerHTML+=response.responseText
            txt=response.responseText
            console.log("--------------------------")
            console.log(txt)
            console.log("--------------------------")
            console.log(data.state);
            */
            el=this.parent().next();
            el.innerHTML=error.responseText
            
        },
        error: function(error) 
        {
            console.log("Inside error")
            console.log(error.responseText);
            //document.getElementById("reg_val").innerHTML=error.responseText
            el=this.parent().next();
            el.innerHTML=error.responseText
        }
    });
}

function enter(ele)
{
    var data = new Object();
    data.type = $(ele).parent().prev().prev().prev().prev().prev().prev().text();
    data.token = $(ele).parent().prev().prev().prev().prev().prev().prev().prev().text();
    data.quotation = $(ele).parent().prev().children(":first").val();
    data.time = $(ele).parent().prev().prev().prev().prev().children(":first").val();
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/quotation',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    });
}

function allocate(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().prev().text();
    data.employee = $(ele).parent().prev().children(":first").val();
    data.partner = "Simran";
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/allocate',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    });   
}

function verify(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().prev().text();
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/verify',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    }); 
    
}
function sendMes(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().prev().prev().prev().text();
    console.log(data.token)
    data.sender = "Simran"
    data.message = $(ele).parent().prev().children(":first").val();
    /*
    var divDoc = document.getElementById("writeContent");
    divDoc.style.visibility = 'hidden';*/
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/message',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    });

}

function getComService()
{
    data = {"hey":"lol"}
    $.ajax({
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        //data: JSON.stringify(data),
        dataType: 'json',
        url: '/getComService',
        success: function (data) {
            console.log("okayyyy");
        },
        error: function(error) {
        console.log(error);
    }
    });
}

function verify(ele)
{
    var x = $(ele).parent().siblings(":first").text()
    data = new Object()
    data.token = x
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/verify',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    });

}

function viewDocs(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().text();
    console.log(data.token)
    
    var divDoc = document.getElementById("writeContent");
    divDoc.style.visibility = "visible";
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/getDocs',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    }); 
}
function checkbox(valuee){
    if(valuee==2)
    {
        var checkboxes1 = document.getElementsByName('select');
        var checkboxesChecked1 = [];
// loop over them all
        for (var i=0; i<checkboxes1.length; i++) {
 // And stick the checked ones onto an array...
            if (checkboxes1[i].checked) {
                checkboxesChecked1.push(checkboxes1[i].value);
            }
        }
        console.log(checkboxesChecked1);
        document.getElementById("show").value = checkboxesChecked1;
        emp = checkboxesChecked1[0];

        var checkboxes = document.getElementsByName('selectTask');
        var checkboxesCheckedTask = [];
// loop over them all
        for (var i=0; i<checkboxes.length; i++) {
 // And stick the checked ones onto an array...
            if (checkboxes[i].checked) {
            checkboxesCheckedTask.push(checkboxes[i].value);
            }   
        }
        document.getElementById("showTask").value = checkboxesCheckedTask;
        empTask= {[checkboxesChecked1[0]] : checkboxesCheckedTask};
        console.log("NOOOOOOOOOO");
    }
}


   function callMe(){
       console.log(empTask);
       //e.preventDefault();
      var formdata = empTask;
      
      $.ajax({
           type: 'POST',
           contentType: 'application/json; charset=utf-8',
           data: JSON.stringify(formdata),
           dataType: 'json',
           url: '/index',
           success: function (data) {
               console.log(data);
           },
           error: function(error) {
           console.log(error);
       }
       });
   }
