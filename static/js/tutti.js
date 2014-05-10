/*!
 * tutti v1.0.0 (http://tutti.kr)
 * Copyright 2014 Tutti, Inc.
 */

$(document).on("click", ".repertory", function() {
	var rep = $(this).data('id');
	var candle = "";
	var groom = "";
	var bride = "";
	var parent = "";
	var walkoff = "";
	var img = "";
	
	switch (rep) {
	case "디즈니":
		candle = "Can you feel the love tonight";
		groom = "He’s Pirate";
		bride = "Tale as old as time";
		parent = "Reflection";
		walkoff = "A whole new world";
		img = "repertory_disney.png";
		break;
	case "지브리":
		candle = "";
		groom = "";
		bride = "";
		parent = "";
		walkoff = "";
		break;
	}
	
	$(".modal-title").html(rep);
	$(".modal-body img").attr("src","../static/images/" + img);
	$(".modal-body ul #candle").html(candle);
	$(".modal-body ul #groom").html(groom);
	$(".modal-body ul #bride").html(bride);
	$(".modal-body ul #parent").html(parent);
	$(".modal-body ul #walkoff").html(walkoff);

});