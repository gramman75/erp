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
	$.ajax({
		url : href,
		data : param,
		async : false,
		success : function(html){
			$("#content").html(html);
		}
	});		
}

var chart_ajax = function(userId){
    		    var id = "div#"+userId+".modal-body";    		   
				$.ajax({
					url : '/erp/util/user/month_graph',
					data : 'userId='+userId,
					async : false,
					success : function(html){			
						$(id).html(html);
					}
				});		
			}

var popup = function(me){
	var $this = $(me);
	alert($this.text());
	$(me).tooltip();
	
}

var get_programs = function(me){
	$.ajax({
		url : '/erp/notice/register/program',
		data : 'applicationId='+me.value,
		async : true,
		success : function(html){			
			$('#selectProgram').html(html);
		}
	});
}

// 메뉴 active
$(document).ready(function(){
	var $navList = $('#nav li a');
	$navList.click(function(){
		var $this = $(this);
		$this.parent().addClass('active');
		$navList.each(function(){
			var $eachThis = $(this);
			if ($eachThis.parent().text() != $this.parent().text()) {
				$eachThis.parent().removeClass('active');
			}
		})
	})
})


