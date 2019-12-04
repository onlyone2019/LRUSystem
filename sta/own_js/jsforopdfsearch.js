//不同pdf设置
$(".changePdf").click(function(){
     var selectId = $(this).attr('id');
     //var pdfshow = document.getElementById("pdfshow");
     var pdfpath = ('/static/pdf/' + selectId +'.pdf').toString();

     $('#pdfshow').remove();
     var emdiv = '<embed id="pdfshow" src="'+pdfpath+'" width="100%" height="700px">';
     $('#mainshow').html(emdiv);
});