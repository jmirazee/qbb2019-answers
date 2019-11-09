/**
 * Copyright 2002, Celera Genomics, Inc.,
 * 45 West Gude Drive, Rockville, Maryland, 20850, U.S.A.
 * All right reserved.
 *
 * File: cdsEntryCommon.js
 *
 * Description:  This file contains javascript functions used in the cdsEntry.
 *
 * $Revision: 1.1 $  $Date: 2004-10-01 22:33:53 $
 *
 */


var loaded = new Array();

function F_loadRollover(image,imageName) {
   	if (image && image.src && (null == image.out || typeof(image.out) == typeof(void(0)))) {
      	s = image.src;
      	image.out = new Image();
      	image.out.src = s;
      	image.over = new Image();

      	if (imageName.lastIndexOf('/') >= 0 || imageName.lastIndexOf('\\') >=0) {
         	s = imageName;
      	} else {
         	i = s.lastIndexOf('/');
         	if (i<0) i = s.lastIndexOf('\\');
         	if (i<0) { s = imageName; }
         	else { s = s.substring(0,i+1) + imageName; }
   		}

    image.over.src = s;
    loaded[image.name] = image;
  	}
}

function F_roll(imageName,over) {
  	if (document.images) {
      	if (over) { imageObject = "over"; }
      	else { imageObject = "out"; }
  		image = loaded[imageName];
   		if (image) {
      		ref = eval("image."+imageObject);
       		if (ref) image.src = eval("image."+imageObject+".src");
   		}
   	}
}

function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}

function clearChecked(form) {
  for (var i=0; i< form.elements.length;i++) {
    tmp= form.elements[i]
    if (tmp.type == "checkbox") tmp.checked=0
  }
}
function checkAll(form) {
  for (var i=0;i < form.elements.length; i++) {
    var tmp = form.elements[i];
    if (tmp.type == "checkbox") tmp.checked = true;
  }
}

function openHelpWindow(helpFile)
{
  theUrl = "/tips/" + helpFile;
  helpWindow = window.open(theUrl, "Help", "scrollbars=yes,resizable=yes,width=640,height=400");
  helpWindow.focus();

}

function trimString (str) {
  str = this != window? this : str;
  return str.replace(/^\s+/g, '').replace(/\s+$/g, '');
}

function checkSearchForm(frm)
{
    var totalLen = 0;
    for (var i =0 ; i < frm.elements.length; i++)
    {                   
        if (frm.elements[i].type == "text"){
            var formValue = frm.elements[i].value;
            formValue = trimString(formValue);
            var len = formValue.length;

            totalLen += len;
            if (formValue.match(/^\s*\*\s*$/) != null){
                alert("Wildcard must be used with keyword.");
                frm.elements[i].focus();
                frm.elements[i].select();
                return false;
            }
            else if (formValue.charAt(len-1) == '&' || formValue.charAt(len-1) == '!' || 
              formValue.charAt(len-1) == '|'){
                alert("Invalid input. & ! and | can not be at the end of search term.");
                frm.elements[i].focus();
                frm.elements[i].select();
                return false;
            }
            else if (formValue.charAt(0) == '&' || formValue.charAt(0) == '!' || 
              formValue.charAt(0) == '|'){
                alert("Invalid input. & ! and | can not be at the begining of search term.");
                frm.elements[i].focus();
                frm.elements[i].select();
                return false;
            }
            else if (formValue.indexOf("||") != -1 || formValue.indexOf("&&") != -1
              || formValue.indexOf("!!") != -1){
              alert("Invalid input!");
              frm.elements[i].focus();
              frm.elements[i].select();
              return false;              
            }    
            else{
              if (formValue.indexOf('(') != -1 || formValue.indexOf(')') != -1){ 
                if ((formValue.indexOf('(') * formValue.indexOf(')')) < 0 
                  || (formValue.indexOf('(') + formValue.indexOf(')')) < 0 ){
                  alert("Unpaired parenthesis!");
                  frm.elements[i].focus();
                  frm.elements[i].select();
                  return false;              
                }else if (formValue.match(/\([^\!\|&]*[a-zA-Z0-9][^\!\|&]*\)/) == null){
                  alert("Invalid input!");
                  frm.elements[i].focus();
                  frm.elements[i].select();
                  return false;
                }
              }
            }
          
        }
    }
    if(totalLen == 0){
       alert("No search term is entered. Please enter your keyword!");
       //frm.focus(); 
       return false;
    }
    return true;
}

function openWindow(url) {
    var winHandle=window.open(url, "productpage", "width=640,height=400,resizable,scrollbars=yes");
    if (winHandle == null)
       alert("Not enought resources to open a new window\n\nPlease close some applications and try again!");
}

function resizeWin(){
  if (navigator.appName.indexOf("Netscape") != -1){
    window.location.href = window.location.href;
  }
}

function enableCheckBoxes (elementName) {
  var boxes = document.getElementsByName(elementName);
  if (boxes != null) {
    for (var i=0;i < boxes.length; i++) {
      boxes[i].disabled = false;
    }
  }
}

function disableCheckBoxes (elementName) {
  var boxes = document.getElementsByName(elementName);
  if (boxes != null) {
    for (var i=0;i < boxes.length; i++) {
      boxes[i].disabled = true;
    }
  }
}

function clearSpecifiedCheckBoxes(elementName) { 
  var boxes = document.getElementsByName(elementName); 
  if (boxes != null) {
    for (var i=0;i < boxes.length; i++) { 
      boxes[i].checked = 0;
    }
  } 
} 
