
/* Displaying result  */
document.addEventListener('DOMContentLoaded', function () {
            document.getElementById('click').click();
          });

/* Input box numbers validation */
var validNumber = new RegExp(/^\d*\.?\d*$/);
    var fist_input = document.getElementById("inlineFormInputGroup").value;
    function validateNumber(elem) {
      if (validNumber.test(elem.value)) {
        fist_input = elem.value;
      } else {
        elem.value = fist_input;
      }
    }