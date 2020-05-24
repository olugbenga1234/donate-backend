<?php
 $firstname = $_Post['firstname'];
 $lastname = $_Post['lastname'];
$user_email = $_Post['email'];


$email_from = 'donateaseedoffcial@gmail.com';

$email_subject = "Registration Confirmation on Donate A Seed";

$email_body = "Hello Mr/Mrs: $lastname.\n".
                "This is a confirmation of your Appliation for Donate A Seed.\n".
                "We will review your application and get back to you on $user_email."
                "Please ignore this message if you did not register on our platform.\n".
                ".\n .\n .\n"
                "Regards.";


mail($email_subject,$email_body)
                

?>
