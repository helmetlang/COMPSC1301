#!/usr/bin/php8.2

<?php
	echo(base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362"))));
?>

# first thing is to take the initial encoded information, and then do a hex 2 bin conversion,
# and then reverse that string, and then decode that base64 information and receive the secret