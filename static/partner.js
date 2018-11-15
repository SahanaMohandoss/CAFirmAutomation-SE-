var empTask= new Object();
var emp;
var sendCon = new Object();
//when document loads


$(document).ready(function() {
    $('.display').DataTable();
} );
function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
        tablinks[i].style.color = "black";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;
    elmnt.style.color = "white";

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function onLoad()
{
    console.log("really?");
    var divDoc = document.getElementById("writeContent");
    divDoc.style.visibility = 'hidden';
    var divDoc = document.getElementById("remDiv");
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
function sendReminder(ele)
{
    var divDoc = document.getElementById("remDiv");
    divDoc.style.visibility = 'hidden';
    var reminder = new Object();
    reminder.reminder_name = $(ele).parent().children(":first").val();
    reminder.generated_by="Simran";
    reminder.timestamp = $(ele).prev().prev().prev().val();
    reminder.curr_timestamp = $(ele).prev().prev().prev().val();
    reminder.reminder_message = $(ele).prev().prev().val();
    reminder.mailing_list = $('#rem').val();

    console.log(reminder);
    $.ajax({ 
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(reminder),
        dataType: 'json',
        url: '/reminder',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
        console.log(error);
    }
    });
}
function createReminder(ele)
{
    var divDoc = document.getElementById("remDiv");
    divDoc.style.visibility = "visible";
}
/*
function enter(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().prev().prev().text();
    data.quotation = $(ele).parent().prev().prev().children(":first").val();
    data.time = $(ele).parent().prev().children(":first").val();
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
*/


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
            $(ele).parent().next().innerHTML=data.responseText
            /*
            response = JSON.parse(data)
            document.getElementById("reg_val").innerHTML+=response.responseText
            txt=response.responseText
            console.log("--------------------------")
            console.log(txt)
            console.log("--------------------------")
            console.log(data.state);
            */
        },
        error: function(error) 
        {
            console.log("Inside error")
            console.log(error.responseText);
            //document.getElementById("reg_val").innerHTML=error.responseText
            $(ele).parent().next().innerHTML=data.responseText
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


$(function() {
    $('.file-download').click(function() {
        console.log("Here in download file")
        var data={}
        data["filename"]= $(this).text()
        var row= $(this).parent().parent()[0]
        console.log(row)
        var Cells = row.getElementsByTagName("td");
        var token = Cells[0].innerText;
        data["token"] = token
        data["desc"]= Cells[2].innerText;
        console.log(data)
        console.log(data)
        $.ajax({
            url: '/filee',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                console.log("ok")
                alert("Your file is dowloaded in the FILES folder")
            },
            error: function(error) {
                    console.log("error")
                
               
            }
        });
    });
});



function viewDocs(ele)
{
    var data = new Object();
    data.token = $(ele).parent().prev().prev().prev().text();
    console.log(data.token)
    
    //var divDoc = document.getElementById("writeContent");
    //divDoc.style.visibility = "visible";
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'json',
        url: '/getDocs',
        success: function (data) {
            console.log("its hereeee");
            console.log(data);
        },
        error: function(error) {
        console.log("well here");
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
  