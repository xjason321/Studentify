var input1 = document.getElementById("new-username");
var input2 = document.getElementById("new-password");
var signup = document.getElementById("signup")
var jsonText = document.getElementById("jsontext")

signup.addEventListener("click", function(){
    var data = {
        "username":input1.value,
        "password":input2.value
    }
    jsonText.innerHTML = JSON.stringify(data)
})