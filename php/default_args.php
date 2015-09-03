<?php
function func($a, $b=1) {
    echo $b;
}
func(1);
func(3, $b=2);
?>