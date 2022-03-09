// Left side hover auth user prop 
function toggle(checked) {
    var elm = document.getElementById("menu-control");
    if (true == elm.checked) {
        document.getElementById("bg-blur").style.display = "none";
    } else if (true != elm.checked) {
        document.getElementById("bg-blur").style.display = "block";
        document.getElementById("bg-blur").style.background = "linear-gradient(90deg,#505050,#505050)";
        document.getElementById("bg-blur").style.opacity = "0.3";
    }
}