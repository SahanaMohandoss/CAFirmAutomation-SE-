
window.onload = function() {
    var reloading = sessionStorage.getItem("reloading");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        console.log("Reload")
        window.location.href = "/clientHome"   
    }
}

   

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
    elmnt.style.color = "white"

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();



function calc()
            {

                typ=document.getElementById("typ").value
                val=document.getElementById("num").value;
                out=document.getElementById("out");
                if(isNaN(parseInt(val)))
                {
                    console.log(typeof(val))
                    out.innerHTML="<font color='red'>Please enter a number</font>"
                    //out.style.backgroundColor="red";
                }
                else
                {
                    console.log(val,typeof(val),isNaN(val),parseInt(val))
                    tax=0
                    sur=0
                    if(typ=="ind1" || typ=="jud")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            if(val<=250000)
                                tax=0
                            else if(val>250000 && val<=500000)
                                tax=(val-250000)*0.05
                            else if(val>500000 && val<=1000000)
                                tax=250000*0.05+(val-500000)*0.2
                            else
                                tax=250000*0.05+500000*0.2+(val-1000000)*0.3
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                        }
                        if(val>5000000 && val<=10000000)
                        {
                            sur=0.1*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else if(val>10000000)
                        {
                            sur=0.15*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else
                        {
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        edcess=0.03*(tax+sur)
                        if(val>=0)
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                    }
                    else if(typ=="ind2")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            if(val<=300000)
                                tax=0
                            else if(val>300000 && val<=500000)
                                tax=(val-300000)*0.05
                            else if(val>500000 && val<=1000000)
                                tax=200000*0.05+(val-500000)*0.2
                            else
                                tax=200000*0.05+500000*0.2+(val-1000000)*0.3
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                        }
                        if(val>5000000 && val<=10000000)
                        {
                            sur=0.1*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else if(val>10000000)
                        {
                            sur=0.15*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else
                        {
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        edcess=0.03*(tax+sur)
                        if(val>=0)
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                    }
                    else if(typ=="ind3")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            if(val<=500000)
                                tax=0
                            else if(val>500000 && val<=1000000)
                                tax=(val-500000)*0.2
                            else
                                tax=500000*0.2+(val-1000000)*0.3
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                        }
                        if(val>5000000 && val<=10000000)
                        {
                            sur=0.1*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else if(val>10000000)
                        {
                            sur=0.15*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        else
                        {
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                        }
                        edcess=0.03*(tax+sur)
                        if(val>=0)
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                    }
                    else if(typ=="part" || typ=="local")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            tax=0.3*val
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                            if(val>10000000)
                                sur=0.12*tax
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                            edcess=0.03*(tax+sur)
                            if(val>=0)
                                out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                        }
                    }
                    else if(typ=="dom")
                    {
                        turn=document.getElementById("turn").value
                        if(val<0 || turn<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            if(turn>500000000)
                            {
                                tax=0.3*val
                            }
                            else
                            {
                                tax=0.25*val
                            }
                            if(val>100000000)
                            {
                                sur=0.12*tax
                            }
                            else if(val>10000000 && val<=100000000)
                            {
                                sur=0.07*tax
                            }
                            else
                                sur=0;
                            edcess=0.03*(tax+sur)
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                        }               
                    }
                    else if(typ=="for")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            tax=0.4*val
                            if(val>100000000)
                            {
                                sur=0.05*tax
                            }
                            else if(val>10000000 && val<=100000000)
                            {
                                sur=0.02*tax
                            }
                            else
                                sur=0;
                            edcess=0.03*(tax+sur)
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                        }
                    }
                    else if(typ=="coop")
                    {
                        if(val<0)
                            out.innerHTML="Please enter a positive number"
                        else
                        {
                            if(val<=10000)
                                tax=0.1*val
                            else if(val>10000 && val<=20000)
                            {
                                tax=1000+(val-10000)*0.2
                            }
                            else if(val>20000)
                            {
                                tax=1000+2000+(val-20000)*0.3
                            }
                            if(val>10000000)
                            {
                                sur=0.12*tax
                            }
                            else
                                sur=0;
                            edcess=0.03*(tax+sur)
                            out.innerHTML="Amount = "+convert(val)+"<br>Tax = "+convert(tax.toFixed(3));
                            out.innerHTML+="<br>Surcharge = "+convert(sur.toFixed(3));
                            out.innerHTML+="<br>Education cess = "+convert(edcess.toFixed(3));
                        }
                    }
                    else
                    {
                        out.innerHTML="Not Calculated Yet"
                    }

                }
            }
            function new_elem()
            {
                console.log("Here atleast")
                typ=document.getElementById("typ").value;
                if(typ=="dom")
                {
                    select=document.getElementById("gross");
                    select.innerHTML+="<br><b>Enter Turnover Amount:&nbsp;</b> <input type='number' id='turn' placeholder='Enter Turnover' />";
                }
                else
                {
                    var select = document.getElementById("gross"); 
                    console.log(select.childNodes);
                  // Get the <ul> element with id="myList"
                    if(select.hasChildNodes())
                    { 
                        select.removeChild(select.childNodes[3]);
                        select.removeChild(select.childNodes[2]);
                        select.removeChild(select.childNodes[1]);
                        select.removeChild(select.childNodes[0]); 
                    }  
                }
            }
            function convert(rup)
            {
                var x=rup
                x=x.toString();
                var afterPoint = '';
                if(x.indexOf('.') > 0)
                    afterPoint = x.substring(x.indexOf('.'),x.length);
                x = Math.floor(x);
                x=x.toString();
                var lastThree = x.substring(x.length-3);
                var otherNumbers = x.substring(0,x.length-3);
                if(otherNumbers != '')
                lastThree = ',' + lastThree;
                var res ="Rs. "+ otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree + afterPoint;
                return res
            }



$(document).ready(
    function(){

    $('form').on('submit', function(e){

      e.preventDefault();
    
      });

    $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
    });
    $('.remove').click(function(){
        console.log($(this).closest('div'))
        $(this).closest('div').slideUp('slow', function(){$(this).remove();});
    });     

    $('#btnUpload').click(function(){
       
        console.log("here")
        var div = document.createElement("div")
        div.className = "formelement"
        var numItems = $('#onefile').length;
        var input =  document.createElement("input")
        input.type = "file"
        input.id = "files"
        input.name = "files[]"
        input.multiple = ""
        div.appendChild(input)
        var img =  document.createElement("img")
        img.src =  "../static/x.gif"
        img.className = "remove"
        img.addEventListener('click', 
            function(){
        $(this).closest('div').slideUp('slow', function(){$(this).remove();})
            }, false);
        div.appendChild(img)
        var text =  document.createElement("input")
        text.type = "text"
        text.name = "filedesc"
        text.id =  "filedesc"
        text.placeholder  = "Enter a file description"
        var br =  document.createElement("br")
         div.appendChild(text)
        div.appendChild(br)
        console.log(img.className)
        var maindiv = document.getElementById("filesdiv")
        maindiv.appendChild(div)
        console.log(maindiv.id)
    });
}
);



$(function() {
    $('#btnFeedback').click(function() {
        console.log("Here")
        var data={}
        data["feedback"]= $('#feedback').val()
        
        var row= $(this).parent().parent()[0]
        console.log(row)
        var Cells = row.getElementsByTagName("td");
        var token = Cells[1].innerText;
        data["token"] = token
        console.log(token)
        console.log(data)
        $.ajax({
            url: '/submitFeedback',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                console.log("ok")
                alert("Feedback added")
                $('#feedback').val('') 
            },
            error: function(error) {
                    console.log("error")
                
               
            }
        });
    });
});



$(function() {
    $('#btnSendMessage').click(function() {
        console.log("Here in send message")
        var data={}
        data["content"]= $('#content').val()
         data["from"]= uname
          data["to"]= $('#to').val()
        console.log(data)
        $.ajax({
            url: '/sendMessage',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                console.log(response.responseText)
                response = JSON.stringify(response)
                response = JSON.parse(response.toString())
                console.log(response["status"]);
                if(response["status"]==0)
                {
                    alert("The username you want to message doesnt exist!")
                }
                else
                {
                console.log("ok")
                alert("Your message has been sent")
                $('#from').val(uname) 
                $('#to').val('') 
                $('#content').val('') 
                }
            },
            error: function(error) {
                    console.log("error")
                
               
            }
        });
    });
});



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
            url: '/fileDownload',
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

$(function() {
    $('.invoice-file-download').click(function() {
        console.log("Here in download file")
        var data={}
        data["filename"]= $(this).text()
        var row= $(this).parent().parent()[0]
        console.log(row)
        var Cells = row.getElementsByTagName("td");
        var token = Cells[0].innerText;
        data["token"] = token
        data["gen"]= Cells[1].innerText;
        data["amt"]= Cells[4].innerText;
        console.log(data)
        console.log(data)
        $.ajax({
            url: '/invoiceFileDownload',
            data: JSON.stringify(data),
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                console.log("ok")
                alert("Your file is dowloaded in the INVOICE folder")
            },
            error: function(error) {
                    console.log("error")
                
               
            }
        });
    });
});



$(function() {
    $('.btnServiceFile').click(function() {
        var data={}
        var form = $(this).parent()
        console.log(form[0])
        var formData = new FormData(form[0]);
        console.log(formData)
    $.ajax({
        url: '/serviceFileUpload',
        type: 'POST',
        data: formData,
        success: function (data) {
            alert("The file has been uploaded")
            form[0].reset()
        },
        cache: false,
        contentType: false,
        processData: false
    });
    });
});










function logOut()
{
    console.log("in logoutx")
    window.location.href = "/logout"
}


function hideDialog() {
  jQuery("#compose-mail").removeClass("visible").addClass("hidden");
}

// At the beginning, we hide the dialog:
hideDialog();

// jQuery("#button-for-compose-mail").on("click", showDialog);

$("#button-for-compose-mail").on("click", function(){
  $("#compose-mail").removeClass("hidden").addClass("visible");
  
  // focus on input.
  $("input#to").focus();
   $("input#from").val(uname);
   $("input#from").prop('readonly', true);
  return false;
});


$(".compose-mail-reply").on("click", function(){
    console.log("Inreply")
  $("#compose-mail").removeClass("hidden").addClass("visible");
  console.log("Inreply")
  var row= $(this).parent().parent()[0]
    console.log(row)
    var Cells = row.getElementsByTagName("td");
    var sender = Cells[0].innerText;
  // focus on input.
  sender = sender.trim()
  $("input#message").focus();
  $("input#to").val(sender);
  $("input#from").val(uname);
  $("input#from").prop('readonly', true);
  return false;
});

$("#close-button").on("click", function(){
  hideDialog();
});

$("form").on("submit", function() {
  hideDialog();
  
  $("input#to").val("")
  $("textarea#content").val("");
  
  // stop browser default behavior.
  // Don't return false if you really want to submit the form, unless you are using AJAX to send the form.
  return false;
});
       


$(function() {
    $('#btnSubmit').click(function() {
        console.log("Here")
        var form = document.querySelector('#myForm');
        var formData = new FormData(form);
        $.ajax({
            url: '/submitRequest',
            data: formData,
            type: 'POST',
            processData: false,
            contentType: false,
            success: function(response) {
                console.log("ok")
                response = JSON.parse(response)
                var t = response["token"]
                alert("YOUR REQUEST HAS BEEN SUBMITTED.\n YOU TOKEN NUMBER IS : "+t+" \nTHE PARTNER WILL BE IN TOUCH WITH YOU WITH THE QUOTATION \nYou can track the status in the view services tab!")
                document.getElementById("myForm").reset();
            },
            error: function(error) {
                    console.log("error")
                
               
            }
        });
    });
});


$('#filterByStatus').change(function(){
    var criteria = $(this).val();
    if(criteria == 'ALL'){
        $('.status').each(function(i,option){
        $(this).parent().show();
        });
        return;
    }
    else
    {
    $('.status').each(function(i,option){
        console.log(($(this).html()), criteria)
        if($(this).html() == criteria){
            $(this).parent().show();
        }else {
            $(this).parent().hide();
        }
    });
    }
});


$('.searchByToken').keyup(function(){
    console.log("IT CHANGED")
    var criteria = $(this).val();
    if(criteria == ''){
        $('.tok').each(function(i,option){
        $(this).parent().show();
        });
        return;
    }
    else
    {
    $('.tok').each(function(i,option){
        console.log(($(this).html()), criteria)
        if($(this).html() == criteria){
            $(this).parent().show();
        }else {
            $(this).parent().hide();
        }
    });
    }
});

