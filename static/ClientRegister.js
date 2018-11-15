

window.onpopstate = function () {
        history.pushState(null, null, window.href);
        history.go(0);
    };

$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});







$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});



$(document).ready(function () {

    toggleFields(); //call this first so we start out with the correct visibility depending on the selected form values
    //this will call our toggleFields function every time the selection value of our underAge field changes
    $("#usertype").change(function () {
        toggleFields();
        document.getElementById("aadhar_error").innerHTML = ""
        document.getElementById("pan_error").innerHTML = ""
        document.getElementById("employeeID_error").innerHTML = ""
    });

    $("#aadhar").change(function () {
         document.getElementById("aadhar_error").innerHTML = ""
        
    });

    $("#number").change(function () {
         document.getElementById("number_error").innerHTML = ""
        
    });

    $("#pan").change(function () {
        document.getElementById("pan_error").innerHTML = ""
        
    });

    $("#employeeID").change(function () {
         document.getElementById("employeeID_error").innerHTML = ""
    });



    $("#username").change(function () {
         document.getElementById("username_error").innerHTML = ""
    });

    $("#firstname").change(function () {
        document.getElementById("firstname_error").innerHTML = ""
    });

    $("#lastname").change(function () {
         document.getElementById("lastname_error").innerHTML = ""
    });

    $("#password").change(function () {
         document.getElementById("password_error").innerHTML = ""
    });

    $("#confpassword").change(function () {
         document.getElementById("confpassword_error").innerHTML = ""
    });

    $("#email").change(function () {
        document.getElementById("email_error").innerHTML = ""
    });

});
//this toggles the visibility of our parent permission fields depending on the current selected value of the underAge field
function toggleFields() {
    if ($("#usertype").val() ==1 || $("#usertype").val() ==2 )
        $("#employee").show();
    else
        $("#employee").hide();
	if ($("#usertype").val() ==0)
        $("#client").show();
    else
        $("#client").hide();
}






$(function() {
    $('#btnSignUp').click(function() {
        console.log("Here")
        var f = document.querySelector('#RegisterForm');
        var formData = new FormData(f);
        $.ajax({
            url: '/signUp',
            data: formData,
            type: 'POST',
            cache: false,
            processData: false,
            contentType: false,
            success: function(response) {
                response = JSON.parse(response)
                console.log(response["status"]);
                if(response["status"]==0)
                {
                console.log("ALL IS OKAY TILL HERE")
                alert("You have been registered with the CA Automation firm! Go ahead and log in")
                document.getElementById("RegisterForm").reset();
                }
                else if(response["status"]==2)
                {
                  if(response["username"]==1)
                  {
                     error = document.getElementById("username_error")
                      error.innerHTML = "This username already exists!"
                  }
                  if(response["email"]==1)
                  {
                     error = document.getElementById("email_error")
                      error.innerHTML = "This email ID already exists!"
                  }
                  if(response["aadhar"]==1)
                  {
                     error = document.getElementById("aadhar_error")
                      error.innerHTML = "This Aadhar number already exists!"
                  }
                  if(response["pan"]==1)
                  {
                     error = document.getElementById("pan_error")
                      error.innerHTML = "This PAN card no already exists!"
                  }
                   
                }
                else
                {
                  console.log("Here")
                  uname = document.getElementById("username").value
                  
                  if(!uname)
                  {
                    error = document.getElementById("username_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid username"
                  }

                  email = document.getElementById("email").value
                  
                  if(!email)
                  {
                    error = document.getElementById("email_error")

                    error.innerHTML = "This field cant be empty! Please enter a valid email ID"
                  }
                  else
                    {var atposition=email.indexOf("@");  
                      var dotposition=email.lastIndexOf(".");  
                      if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){  
                        error = document.getElementById("email_error")
                        error.innerHTML = "Invalid email ID! Please enter a valid email ID"

                      }
                    }

                  firstname = document.getElementById("firstname").value
                  
                  if(!firstname)
                  {
                    error = document.getElementById("firstname_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid Firstname"
                  }

                  number = document.getElementById("number").value
                  
                  if(!number)
                  {
                    error = document.getElementById("number_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid Number"
                  }


                  lastname = document.getElementById("lastname").value
                  
                  if(!lastname)
                  {
                    error = document.getElementById("lastname_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid Lastname"
                  }
                  if(document.getElementById("usertype").value == 0)
                  {
                    adhaar = document.getElementById("aadhar").value
                  
                    if(!adhaar)
                    {
                      error = document.getElementById("aadhar_error")
                      error.innerHTML = "This field cant be empty! Please enter a valid Adhaar number"
                    }

                    pan = document.getElementById("pan").value
                    
                    if(!pan)
                    {
                      error = document.getElementById("pan_error")
                      error.innerHTML = "This field cant be empty! Please enter PAN number"
                    }

                  }
                  else
                  {
                     employeeID = document.getElementById("employeeID").value
                  
                    if(!employeeID)
                    {
                      error = document.getElementById("employeeID_error")
                      error.innerHTML = "This field cant be empty! Please enter a valid employeeID"
                    }
                  }
                  
                  password = document.getElementById("password").value
                  
                  if(!password || password.length<6)
                  {
                    error = document.getElementById("password_error")
                    error.innerHTML = "Please enter a password of atleast 6 characters"
                  }

                  confpassword = document.getElementById("password").value
                  
                  if(!confpassword)
                  {
                    error = document.getElementById("confpassword_error")
                    error.innerHTML = "Please enter a password of atleast 6 characters"
                  }
                  else
                  {
                    if(!(confpassword===(password)))
                    {
                      error = document.getElementById("confpassword_error")
                      error.innerHTML = "The password and confirm password fields do not match!"
                    }

                  }
                } 
            },
            error: function(error) {

                
                console.log(error);
            }
        });
    });
});





$(function() {
    $('#btnLogIn').click(function() {
        console.log("Here IN LOG IN")
        $.ajax({
            url: '/logIn',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                response = JSON.parse(response)
                console.log(response["status"]);
                if(response["status"]==0)
                {
                    console.log("username doesnt exist")
                    alert("The username does not exist! Maybe you want to sign up first!")
                  
                } 
                else if(response["status"]==2)
                {
                  console.log("wrong password")
                    alert("Incorrect password!")
                }
                else
                { 
                  
                    console.log(response['type'])
                    if(response['type']==0){
                        window.location.href = "/clientHome"
                      }
                    else if(response['type']==1){
                    	window.location.href = "/EmployeeHome"
                    }
                    else{
                        window.location.href = "/partner"   
                        }
                }
            },
            error: function(error) {

                
                console.log(error);
            }
        });
    });
});




$(document).ready(
    function(){

    

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
        //input.id = "files"
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
