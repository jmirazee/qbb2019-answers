function strtrim(str) {
  return str.replace(/^\s+/,'').replace(/\s+$/,'');
}

//page one
function focusForm() {
  document.regform.userFirstName.focus();
}

function selectSelect(pre_value, select_object)
{
  len = select_object.length;
  for(i=0; i < len; i++){
    if(select_object.options[i].value == pre_value){
      select_object.options[i].selected= true;
      break;
    }
  }
}

function checkEmailAddress(email, email_name)
{
  var message = "";
  var re = /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*\.[a-zA-Z]+$/gi;
  email.value = strtrim(email.value);
  var result = email.value.match(re);
  if(result == null)
    message = email_name + " invalid format\n";
  return message;

}
function checkMatchField(field1, field_name1, field2, field_name2 )
{
  var message = "";
  if( field1.value != field2.value)
    message += field_name1 + " and "+ field_name2 +" don't match.\n";
  return message;
}

function checkField(theTextField, fieldname, mini_length, max_length)
{
  var message = "";
  if (theTextField != null){
    var checkChar = checkValidChars(theTextField, fieldname);
    theTextField.value = strtrim(theTextField.value);
    if(max_length != null){
      var message1 =  checkTextUpLimit(max_length, theTextField.value.length, fieldname);
      var message2 =  checkTextDownLimit(mini_length, theTextField.value.length, fieldname);
      message += message1;
      message += message2;
      if(message1.length == 0 && message2.length== 0){
        if (checkChar.length != 0){
          message = message + checkChar ;
        }
      }
    }else if(mini_length != null){
      var message1 =  checkTextDownLimit(mini_length, theTextField.value.length, fieldname);
      message += message1;
      if(message1.length == 0 ){
        if (checkChar.length != 0 ){ 
          message = message +  checkChar;
        }
      }
    }else{
      if (checkChar.length != 0 ){
        message = message + checkChar;
      }
    }
  }
  return message;
}

function checkTextUpLimit(limit, leng, label)
{
  if(leng > limit)
    return label + " can't exceed length of " + limit + "\n";
  else
    return "";
}

function checkTextDownLimit(limit, leng, label)
{
  if(leng < limit){
    if(limit == 1)
      return label + " required\n";
    else
      return label +" requires of minimum length of " + limit + "\n";
  }
  else
    return "";
}
                 
function checkSelect(theSelectField, missingField, fieldname)
{
  if (theSelectField.options[theSelectField.selectedIndex].value.trim() == ""){
    missingField += fieldname+" required\n";
  }
  return missingField;
}

function checkValidChars(fieldObj, fieldLabel)
{
  var var1 = fieldObj.value;
  if (fieldObj.name == 'passwd' || fieldObj.name == 'vfpasswd') {
    // No spaces allowed in password fields   
    re = new RegExp("[^\\w\-\.@\_]", "gi");
  }
  else {
    re = new RegExp("[^\\w\-\.@ \_]", "gi");
  }

  if (var1.length > 0 && re.test(var1)) {
    var retMsg = "Invalid character(s) in " + fieldLabel + ". Allowed characters are [a-z], [A-Z], 0-9 and '_' , '-' , '.' and '@'." + "\n";
    return retMsg;
  }
                 
  return "";
}

function validateUserForm(f)
{
  var missingField = "";
  missingField += checkField(f.userFirstName, "First Name", 1, 30);
  missingField += checkField(f.userLastName, "Last Name", 1, 30);
  missingField += checkField(f.logid, "User ID", 6, 15);
  missingField += checkField(f.passwd, "Password", 6, 15);
  missingField += checkField(f.vfpasswd, "Verify Password", 6, 15);
  missingField += checkField(f.email, "E-mail", 1, 100);
  missingField += checkField(f.vfemail, "Verify E-mail", 1, 100);
  missingField += checkField(f.organization, "Organization", 1, 35);
  missingField += checkField(f.country, "Country", 1, 30);
  missingField += checkEmailAddress(f.email,"Contact E-Mail");
  missingField += checkEmailAddress(f.vfemail,"Verify E-Mail");
  missingField += checkMatchField(f.passwd, "Password", f.vfpasswd, "Password Verification");
  missingField += checkMatchField(f.email,"Contact E-Mail",f.vfemail,"Verify Contact E-Mail");
   
  if (missingField != "") {
    alert("There were some errors found.\n Please enter/correct the following fields:  \n\n" +
      missingField);
    return false;
  }        
  return true;
}
  
function submitUserForm(){  
  if(validateUserForm(document.regform)){
    document.regform.passwd.value = hex_md5(document.regform.passwd.value);
    document.regform.vfpasswd.value = hex_md5(document.regform.vfpasswd.value);
    document.regform.submit();
  }else{
    focusForm();
  }
}

function cancelUserForm(redirectURL){
  location.href = redirectURL;
}

function validateChangePasswdForm(f){
  var missingField = "";
  missingField += checkField(f.oldpasswd, "Old password", 6, 15);
  missingField += checkField(f.newpasswd, "New password", 6, 15);
  missingField += checkField(f.cfpasswd, "Confirm new password", 6, 15);
  missingField += checkMatchField(f.newpasswd, "New password", f.cfpasswd, "Confirm new password");
 
  if (missingField != "") { 
    alert("There were some errors found.\n Please enter/correct the following fields:  \n\n" +
      missingField);
    return false;
  }
  return true;
}

function submitChangePasswdForm(passwd){
  if(validateChangePasswdForm(document.cgpwdform)){
    document.cgpwdform.oldpasswd.value = hex_md5(document.cgpwdform.oldpasswd.value);
    // verify old password
    if (passwd != document.cgpwdform.oldpasswd.value){
       alert("Old password is incorrect! Please try again.");
       return;
    }else{
      document.cgpwdform.newpasswd.value = hex_md5(document.cgpwdform.newpasswd.value);
      document.cgpwdform.cfpasswd.value = hex_md5(document.cgpwdform.cfpasswd.value);
      document.cgpwdform.submit();
    }
  }else{
    document.cgpwdform.oldpasswd.focus();
  }
}

function validateForgetPasswdForm(f){
  var missingField = "";
  missingField += checkField(f.logid, "User ID", 6, 15);
 
  if (missingField != "") {
    alert(missingField);
    return false;
  }
  return true;
}
    
function submitForgetPasswdForm(){
  if(validateForgetPasswdForm(document.forgetpwdform)){
    document.forgetpwdform.submit();
  }else{
    document.forgetpwdform.logid.focus();
  }
}

function validateChangeEmailForm(f){
  var missingField = "";
  missingField += checkField(f.email, "E-Mail", 1, 100);
  missingField += checkEmailAddress(f.email,"E-Mail");
 
  if (missingField != "") { 
    alert("There were some errors found.\n Please enter/correct E-Mail address:  \n\n" +
      missingField);
    return false;
  }
  return true;
}

function submitChangeEmail(){
  if(validateChangeEmailForm(document.cgemailform)){
    document.cgemailform.submit();
  }else{
    document.cgemailform.email.focus();
  }  
}

function submitSubscription(){
  if(validateChangeEmailForm(document.subscriptionform)){
    document.subscriptionform.submit();
  }else{
    document.subscriptionform.email.focus();
  }  
}

function add2MailingList(cid){
  location.href = "/servlet/com.ab.scienceSite.servlet.MailingList?action=add&cid=" + cid;
}

function removeFromMailingList(cid){
  location.href = "/servlet/com.ab.scienceSite.servlet.MailingList?action=remove&cid=" + cid;
}

function submitUnsubscription(){
  if(validateChangeEmailForm(document.unsubscriptionform)){
    document.unsubscriptionform.submit();
  }else{
    document.unsubscriptionform.email.focus();
    return false;
  }  
}