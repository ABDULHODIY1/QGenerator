document.addEventListener("DOMContentLoaded", function () {
    var modal = document.querySelector(".cont-cr");
    var openButton = document.querySelector("#openForm");
    var closeButton = document.querySelector("#closeForm");

    openButton.addEventListener("click", function () {
      modal.style.display = "flex";
    });

    closeButton.addEventListener("click", function () {
      modal.style.display = "none";
    });
  });
  