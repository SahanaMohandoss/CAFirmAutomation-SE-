var empTask= new Object();
var emp;
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
console.log(empTask);

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