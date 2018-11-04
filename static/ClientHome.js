


    window.onpopstate = function () {
        history.pushState(null, null, location.href);
        history.go(1);
    };

function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;

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
        var input =  document.createElement("input")
        input.type = "file"
        input.id = "files"
        input.name = "files[]"
        input.multiple = ""
        div.appendChild(input)
        var img =  document.createElement("img")
        img.src =  'http://images.freescale.com/shared/images/x.gif'
        img.className = "remove"
        img.addEventListener('click', 
            function(){
        $(this).closest('div').slideUp('slow', function(){$(this).remove();})
            }, false);
        div.appendChild(img)
        console.log(img.className)
        var maindiv = document.getElementById("filesdiv")
        maindiv.appendChild(div)
        console.log(maindiv.id)
    });
}
);



function searchByToken() {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}



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
       
