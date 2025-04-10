document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript Loaded!");
});


<script>
  function validate() {
    const form = document.forms["myForm"];

    if (form["Name"].value.trim() === "") {
      alert("Please provide your name!");
      form["Name"].focus();
      return false;
    }

    if (form["EMail"].value.trim() === "") {
      alert("Please provide your Email!");
      form["EMail"].focus();
      return false;
    }

    if (
      form["Zip"].value.trim() === "" ||
      isNaN(form["Zip"].value) ||
      form["Zip"].value.length !== 5
    ) {
      alert("Please provide a zip in the format #####.");
      form["Zip"].focus();
      return false;
    }

    if (form["Country"].value === "-1") {
      alert("Please select your country!");
      form["Country"].focus();
      return false;
    }

    return true;
  }
</script>