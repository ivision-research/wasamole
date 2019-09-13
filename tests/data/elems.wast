;; Taken from:
;;
;; https://github.com/WebAssembly/testsuite/blob/master/elem.wast
(module
  (table $t 10 funcref)
  (func $f)
  (elem (i32.const 0))
  (elem (i32.const 0) $f $f)
  (elem (offset (i32.const 0)))
  (elem (offset (i32.const 0)) $f $f)
  (elem 0 (i32.const 0))
  (elem 0x0 (i32.const 0) $f $f)
  (elem 0x000 (offset (i32.const 0)))
  (elem 0 (offset (i32.const 0)) $f $f)
  (elem $t (i32.const 0))
  (elem $t (i32.const 0) $f $f)
  (elem $t (offset (i32.const 0)))
  (elem $t (offset (i32.const 0)) $f $f)
)
