<?php
function func() {
    $a=array();
    $a['data'] = 1;
    $a['foo'] = 2;
    return $a;
}
print func()['data'];
print (string)in_array('data', array_keys(func()));
print (string)in_array('foo', array_keys(func()));
print var_export(func());
?>