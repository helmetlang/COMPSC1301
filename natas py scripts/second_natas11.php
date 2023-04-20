#!/usr/bin/php8.2
<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {

    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$plaintext = json_encode($defaultdata);
$ciphertext = hex2bin('306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36');
$key = 'KNHL';

$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

$good_plaintext = json_encode($good_data);
$good_ciphertext = xor_encrypt($good_plaintext, $key );

$cookie = base64_encode($good_ciphertext);
echo($cookie);

# XOR
	# plaintext ^ key = cipher text
	# plaintext ^ ciphertext = key

?>

