var getform = function(element, parent){
	var ret ="";
	var Length = $(element, parent).length;
	
	var idnamelist = new Array();
	var idvaluelist = new Array();
	
	for (var i=0; i < Length;i++){
		idnamelist[i] = $(element, parent)[i].name;
		idvaluelist[i] = $(element, parent)[i].value;
		ret += idnamelist[i] + '=' + idvaluelist[i];
		if (i < Length - 1)
			ret += "&";
	}
	
	return ret;
	
}


var content_ajax = function(href,param){
	var callback = function(dataReceived){
		$(this).hide();
		$('#content').html(dataReceived);		
	};
	
	$.ajax({
		url : href,
		data : param,
		async : false,
		success : function(html){			
			$("#content").html(html);
		}
	});		
}



var popup = function(me){
	
	var val = $(me);	
	alert(val.text());
}
