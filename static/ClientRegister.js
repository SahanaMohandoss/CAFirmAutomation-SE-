
//Prevent the file from going back
window.onpopstate = function () {
        history.pushState(null, null, window.href);
        history.go(0);
    };


//For dynamic change in label in form when user types in text area
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





//To enable tabs

$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});


//Things to do as soon as the document is ready
$(document).ready(function () {

    toggleFields(); //call this first so we start out with the correct visibility depending on the selected form values
    //this will call our toggleFields function every time the selection value of our underAge field changes
    //Toggle fields is to change the form registration fields depending on type of user
    $("#usertype").change(function () {
        toggleFields();
        document.getElementById("aadhar_error").innerHTML = ""
        document.getElementById("pan_error").innerHTML = ""
        document.getElementById("employeeID_error").innerHTML = ""
    });
    //clear out all the divs that display errors
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





//sign up for client, employee, register
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
                  //username alrwady exists
                  if(response["username"]==1)
                  {
                     error = document.getElementById("username_error")
                      error.innerHTML = "This username already exists!"
                  }
                  //email exists
                  if(response["email"]==1)
                  {
                     error = document.getElementById("email_error")
                      error.innerHTML = "This email ID already exists!"
                  }
                  //aadhaar exists
                  if(response["aadhar"]==1)
                  {
                     error = document.getElementById("aadhar_error")
                      error.innerHTML = "This Aadhar number already exists!"
                  }
                  //PAN exists
                  if(response["pan"]==1)
                  {
                     error = document.getElementById("pan_error")
                      error.innerHTML = "This PAN card no already exists!"
                  }
                   
                }
                else
                {
                  //Incase password or username or email is empty
                  console.log("Here")
                  uname = document.getElementById("username").value
                  //username empty
                  if(!uname)
                  {
                    error = document.getElementById("username_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid username"
                  }

                  email = document.getElementById("email").value
                  //email empty
                  if(!email)
                  {
                    error = document.getElementById("email_error")

                    error.innerHTML = "This field cant be empty! Please enter a valid email ID"
                  } //email wrong format
                  else
                    {var atposition=email.indexOf("@");  
                      var dotposition=email.lastIndexOf(".");  
                      if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){  
                        error = document.getElementById("email_error")
                        error.innerHTML = "Invalid email ID! Please enter a valid email ID"

                      }
                    }

                  firstname = document.getElementById("firstname").value
                  //firstname empty
                  if(!firstname)
                  {
                    error = document.getElementById("firstname_error")
                    error.innerHTML = "This field cant be empty! Please enter a valid Firstname"
                  }

                  number = document.getElementById("number").value
                  //number field empty
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
                  //check for aadhaar and pan only for clients
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
                      //employee id for partner and employee
                     employeeID = document.getElementById("employeeID").value
                  
                    if(!employeeID)
                    {
                      error = document.getElementById("employeeID_error")
                      error.innerHTML = "This field cant be empty! Please enter a valid employeeID"
                    }
                  }
                  
                  password = document.getElementById("password").value
                  //pass of min length 6
                  if(!password || password.length<6)
                  {
                    error = document.getElementById("password_error")
                    error.innerHTML = "Please enter a password of atleast 6 characters"
                  }

                  confpassword = document.getElementById("password").value
                  //CCheck if pass === conf pass
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



//Log in

$(function() {
    $('#btnLogIn').click(function() {
        console.log("Here IN LOG IN")
        $.ajax({
            url: '/logIn',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
              //Render template accordin to type of user
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

    //Prevent submit due to enter

    $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
    });
    //to cancel file upload
    $('.remove').click(function(){
        console.log($(this).closest('div'))
        $(this).closest('div').slideUp('slow', function(){$(this).remove();});
    });     
    //To upload multiple files
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
