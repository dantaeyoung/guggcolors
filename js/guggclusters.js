$( document ).ready(function() {
	$(".entry").hover(function() {
		$(this).addClass("hovering");
	}, function() {
		$(this).removeClass("hovering");
	});
});
