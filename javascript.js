
/* AJAX
Step - 1. Call the document load function.

$(document).ready(function() {

            Step 2 : Call the action on submit evenet :

            $('form') .on ( 'submit' , function(event){

                   Step 3:  Call the Ajax Function

                   $.ajax( {

                    Step 4: Create here the data for the field values. Request Method 'POST' OR 'GET' and Url for Processing the form.
						data : {
						key1: $('attribute').val(),
						key2: $('attribute').val(),
						.
						.
						keyn: $('attribute').val()

						}
						type : 'POST' OR 'GET'
						url : '/example'

                   } )

				   Step 5: Call the success function.

				   .done(function(data) {

                      Step 6 : Wrtite the code for the data retured from the Server url: '/example'

				   });

				   Step 7 : Prevent the enitre submit event to do default action
                                   event.preventDefault();

            } );

} );

 */