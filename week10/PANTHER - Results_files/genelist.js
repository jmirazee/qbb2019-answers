function listAction(form, url, itemCount, target) {
  if (url == "") {
    return;
  }
  if (target != null) {
    form.target = target;
  } else {
    var totalItemCount = itemCount;
    var itemList = form.genelist;
    var selectedItems = "all";
    var selectedItemCount = 0;
    for (i=0; i<itemList.length; ++i) {
      if (itemList[i].checked) {
        selectedItemCount++;
      }
    }
    if (selectedItemCount > 0) {
      totalItemCount = selectedItemCount;
		selectedItems = "checked";
    }
	 if (url.indexOf("abassaysgateway.jsp") != -1) { // ab assay popup
      form.target = "myscience";
      if (totalItemCount > 100) {
	     if (!confirm("You selected " + totalItemCount + " items. It will be slow for searching more than 100 ids. Are you sure you want to proceed?"))
	     return;
      }
    } else
      form.target = "_self";
  }
  form.action = url + "&save=yes&basketItems=" + selectedItems;
  form.submit();
}

function changeGLAUnsupportedListTypes() {
	 alert("You can only purchase AB Genomic Products for the following list types:\n  Genes\n Transcripts\\Proteins\n" +
	       "Please convert the list.");
}

function changeListPref(form, url, windowUrl, target) {
  form.target = target;
  MM_openBrWindow(windowUrl, target,'scrollbars=yes,resizable=yes,width=550,height=500');
  form.action = windowUrl + "&refreshUrl=" + url + "&save=yes";
  form.submit();
}


function submitNumPerPageGeneList(form, form2) {
  if (form != null) {
    numPerPage = 0;
    for (var i = 0; i < form2.numPerPage.length; i++) {
      if (form2.numPerPage.options[i].selected) {
        numPerPage = form2.numPerPage.options[i].value;
        break;
      }
    }
	var listType = form.listType.value;
    form.action = form.action + "?numPerPage=" + numPerPage +
				"&save=yes&searchModType=numperpage&listType="+listType;
    form.submit();
    return false;
  }
}

function submitHMMCutoffPlusGeneList(form, form2) {
  if (form != null) {
    var cutoff = form2.cutoff.value;
	/*if (!cutoff.match(/ [-+]? ([0-9]* \.)? [0-9]+ ( [eE][-+]? [0-9]+ )? /) || cutoff < 0) {
	  alert("The HMM score cutoff you entered is not a valid number. Please try again.");
	  form2.cutoff.focus();
	  form2.cutoff.select();
	  return false;
	} else {*/
		var listType = form.listType.value;
	form.action = form.action + "?cutoff=" + cutoff + "&save=yes&searchModType=scorecutoff&listType="+listType;
      form.submit();
      return false;
	//}
  }
}

