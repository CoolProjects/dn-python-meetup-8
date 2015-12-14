<?php
$url = "https://translate.google.com/translate_a/single?client=t&sl=en" .
       "&tl=hi&dt=t&ie=UTF-8&oe=UTF-8&otf=1&rom=1&ssel=0&tsel=4&kc=1&tk=90490.476423&hl=en&q=";

// $url = "https://translate.google.com/translate_a/single?client=t&sl=en&tl=hi" .
//        "&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&" .
//        "ie=UTF-8&oe=UTF-8&source=btn&rom=1&ssel=0&tsel=3&kc=0&tk=529025.931794&" .
//        "q=";

$url .= $argv[1];
$content = file_get_contents($url);

print($content);
echo "\n";