;; Taken from:
;;
;; https://github.com/WebAssembly/testsuite/blob/master/start.wast
(module
  (func $a (return (i32.const 0)))
  (func $b (return (i32.const 1)))
  (func $c (return (i32.const 2)))

  (start $c)
)
