(function() {
    var subForm = document.getElementsByName("subscriptionform");
    if (undefined !== subForm && null !== subForm && subForm.length > 0) {
        if (undefined === subForm[0].email) {
            return;
        }
        subForm[0].email.focus();
    }
})();


