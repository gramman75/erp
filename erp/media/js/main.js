var content_ajax = function(href){
	var callback = function(dataReceived){
		$(this).hide();
		$('.content').html(dataReceived);		
	}
		
	$.get(href,null,callback,'html');
};

$(document).ready(function(){	
	var vNav = $('div.vNav');
	var vNav_i = vNav.find('>ul>li>a');
	var vNav_ii = vNav.find('>ul>li>ul>li>a');
	vNav_i.find('ul').hide();
	vNav_i.click(function(){
		$(this).siblings('ul').slideToggle('fast');
		}).trigger('click');

	vNav_ii.click(function(){	
		$(this).parent().toggleClass('active');
	})

})