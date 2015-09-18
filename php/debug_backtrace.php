<?php
function func2($a, $b=2) {
    $data = debug_backtrace();
    foreach ($data as $f) {
        print $f['function'] . " : " . $f['file'] . " : " . $f['line'] . "\n" ;
        print_r($f['args']);
        print "\n";
        print "\n";
    }
}
function func1() {
    func2(1, 3);
}

func1();
?>