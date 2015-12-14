<?php

// $url = "https://translate.google.com/translate_a/single?client=t&sl=en&hl=en&" .
//        "dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&rom=1&ssel=0&tsel=0&kc=2&tk=21140.423657&q=";
$url = "https://translate.google.com/translate_a/single?client=t&sl=en&tl=hi" .
       "&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&" .
       "ie=UTF-8&oe=UTF-8&source=btn&rom=1&ssel=0&tsel=3&kc=0&tk=529025.931794&" .
       "q=";

$i = 0;
$phrase = "i love you";

$to = array(
    'es' => 'Spanish',
    'ne' => 'Nepali',
    'hi' => 'Hindi',
    'nl' => 'Dutch',
    'fi' => 'Finish',
    'fr' => 'French',
    'iw' => 'Hibrew',
    'ja' => 'Japanese',
    'zh-CN' => 'Chinese Simplified',
    'ko' => 'Korean');

echo "Translation of '" . $phrase . "' into " . count($to) . "langauges:\n";
foreach($to as $key => $val) {
    $translate_url = $url . "/" . urlencode($phrase);
    $translate_url .= "&tl=" . $key;

    echo "\n" . ++$i . ". " . $val . "\n";

    $content = file_get_contents($translate_url);

    print($content);
    echo "\n";
}