var button = document.getElementById("brickwall"),
  count = 0;
button.onclick = function () {
  count += 1;
  if (count >= 20) {
    document.getElementById("brickwall").style.display = "none";
    document.getElementById("changetext").innerHTML =
      "You broke the 4th wall! Now you gotta go to the repo and fix it!";
    document.getElementById("github").style.display = "block";
  }
};
