(module 
  (func) (export "a" (func 0))
  (func) (export "b" (func 0))

  (global i32 (i32.const 0)) (export "c" (global 0))
  (global i32 (i32.const 0)) (export "d" (global 0))

  (table 0 funcref) (export "e" (table 0))

  (memory 0) (export "f" (memory 0))
)
