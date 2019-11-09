function submitQuickSearch(){
  var value = quicksearch.fieldValue.value;
  value = value.replace(/^\s*/, '').replace(/\s*$/, ''); 
  if(value===""){
    return;
  }
  var listType = quicksearch.listType.value;
  if(listType==='1'){
    quicksearch.action = '/genes/geneList.do';
  }
  else if(listType==='8'){
    quicksearch.organism.value = "all";
    quicksearch.action = '/pathway/pathwayList.do';
  }
  else if(listType==='6'){
    quicksearch.organism.value = "all";
    quicksearch.action = '/panther/familyList.do';
  }
  else if(listType==='5'){
    quicksearch.organism.value = "all";
    quicksearch.action = '/panther/categoryList.do';
  }
  else {
    quicksearch.organism.value = "all";
    quicksearch.action = '/panther/globalSearch.do?';  
  }
  quicksearch.submit();
}


