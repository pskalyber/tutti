/*!
 * tutti v1.0.0 (http://tutti.kr)
 * Copyright 2014 Tutti, Inc.
 */

$(document).on("click", ".repertory", function () {
     var rep = $(this).data('id');
     $(".modal-title").html(rep);
     $(".modal-body #repertoryName").prepend(rep);
});