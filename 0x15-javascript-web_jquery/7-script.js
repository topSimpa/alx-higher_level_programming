$.get( "https://swapi-api.hbtn.io/api/people/5/?format=json", function( response ) {
    $('DIV#character').text( response['name'] ); // server response
});
