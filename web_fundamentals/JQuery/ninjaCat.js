// $('img').click(function() {
//     console.log('data-alt-src value is', $(this).attr('data-alt-src'));
//   });
  
$('img').click(function() {
    // temp = $(this).attr('src');
    // $(this).attr('src') = $(this).attr('data-alt-src');
    // $(this).attr('data-alt-src') = temp;
    $(this).attr( 'temp', $(this).attr('src')      );
    $(this).attr( 'src', $(this).attr('data-alt-src')    );
    $(this).attr(   'data-alt-src', $(this).attr('temp') )      ;

});


