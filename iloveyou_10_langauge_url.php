<?php

$url = "https://translate.google.com/#en/";
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
    $translate_url = $url . $key . "/" . urlencode($phrase);

    echo ++$i . ". " . $val . ": " . $translate_url . "\n";

    $content = file_get_contents($translate_url);

    echo $content;

}