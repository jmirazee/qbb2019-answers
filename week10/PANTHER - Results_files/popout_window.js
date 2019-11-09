
var popupDefaultWidth = 600;
var popupInfoSize = 400;
var defaultWidth=400;
var defaultHeight=400;

function popout_window(filePath, width, height) {
  if (width == null)
    width = defaultWidth;
  if (height == null)
    height = defaultHeight;
  window.open(filePath, '', "width="+width+",height="+height+",alwaysRaised=yes,status=no,scrollbars=yes");
}

/**
This function is an exact duplicate of popout_window().  popout_window
just wasn't working in pathwayDetail.jsp so we created a copy function
that does work! Go figure!
--Baq Haidri
**/
function popoutWindowPlease(filePath, width, height) {
  if (width == null)
    width = defaultWidth;
  if (height == null)
    height = defaultHeight;
  window.open(filePath, '', "width="+width+",height="+height+",alwaysRaised=yes,status=no,scrollbars=yes");
}

function openInfoWindow(filePath){
  window.open(filePath,'popup','scrollbars=yes,resizable=yes,width='+popupInfoSize+',height='+popupInfoSize+'');
}

function openPopupTarget(filePath, target){
  window.open(filePath, target, 'scrollbars=yes,resizable=yes,width='+popupDefaultWidth+',height='+popupInfoSize+'');
}

function openPopupWithFocus(filePath, target, width, height) {
  if (width == null)
    width = popupDefaultWidth;
  if (height == null)
    height = popupInfoSize;
  var newwindow = window.open(filePath, target, 'scrollbars=yes,resizable=yes,width='+width+',height='+height+'');
  if (window.focus)
    newwindow.focus();
}