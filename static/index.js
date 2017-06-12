$(document).ready(function(){

  $(".sinal").click(function(){
    $(this).closest(".tabela").find("td").toggle();
    var sinal= $(this).text();
    $(this).text( (sinal == "-") ? "+":"-" );
  });

  $('#tresposta').click(function(){
      var site;
      site = $(this).attr("site");
      $.get('site', {dominio: site}, function(resposta){
         $('#site_info').html(resposta);
         $('#site_info').show();
         $('#tresposta').html("Obter Informações Novamente");
         $('#acessar_site').attr("href", site)
         $('#acessar_site').show();
      });
  });

  //function copyToClipboard(element) {
    //var $temp = $("<input>");
    //$("body").append($temp);
    //$temp.val($(element).text()).select();
    //$("")
    //document.execCommand("copy");
    //$temp.remove();
  //}

});
$(window).load(function(){
  $('.teste').hide();
});
