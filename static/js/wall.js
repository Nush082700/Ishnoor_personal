window.onload = function () {
  var count = 0;
  var i = 0;
  var txt =
    "You broke the fourth wall! Now you have to go to the repo to fix it!";
  var speed = 50;
  document.getElementById("brickwall").onclick = function () {
    count += 1;
    if (count >= 20) {
      document.getElementById("brickwall").style.visibility = "hidden";
      document.getElementById("changetext").innerHTML = "";
      document.getElementById("github").style.visibility = "visible";
      typeWriter();
    }
  };

  function typeWriter() {
    if (i < txt.length) {
      document.getElementById("changetext").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  }
};
