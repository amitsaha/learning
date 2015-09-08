<?php
class MyClass {

    private function myfun1() {
        print 'myfun1 called'."\n";
    }
    public static function myfun() {
        print 'Myfun called'."\n";
        static::myfun1();
    }
}

MyClass::myfun();
?>