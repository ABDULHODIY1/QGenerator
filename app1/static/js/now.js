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

  function openDeleteConfirmation(postId) {
    var popup = document.getElementById('delete-confirmation');
    popup.style.display = 'block';

    var deleteButton = document.getElementById('confirm-delete');
    deleteButton.setAttribute('data-post-id', postId);
  }

  function closeDeleteConfirmation() {
    var popup = document.getElementById('delete-confirmation');
    popup.style.display = 'none';
  }
  function deletePost() {
    var deleteButton = document.getElementById('confirm-delete');
    var postId = deleteButton.getAttribute('data-post-id');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/posts/delete/' + postId + '/', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
      if (xhr.status === 200) {
        var postElement = document.getElementById('post-' + postId);
        postElement.parentNode.removeChild(postElement);

        closeDeleteConfirmation();
      }
    };
    xhr.send();
  }