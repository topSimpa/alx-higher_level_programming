$.get( "https://swapi-api.hbtn.io/api/films/?format=json", function( response ) {
    let films = response['results']
    for ( film in films ) {
      $( '<li></li>' ).text( films[film]['title'] ).appendTo( 'UL#list_movies' );
          // server response
});
