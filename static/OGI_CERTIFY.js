function show_alert_box()
{
var x=document.getElementById("input_mail_for_certificate").value;
console.log(x);
    if(x=='')
    {
        alert("You need to enter your mail ")
    }

}