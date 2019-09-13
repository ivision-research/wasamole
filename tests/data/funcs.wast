(module
  (func $func0 (result i32)
    (return (i32.const 0)))

  (func $func1 (result i64)
    (return (i64.const 1)))

  (func $func2 (param i32 f32 i64 f64) (result i64)
    (return (i64.const 2)))

  (func $fib (param $n i32) (result i32)
    (if (i32.lt_s (get_local $n) (i32.const 2))
      (return (i32.const 1)))

    (return (i32.add (call $fib (i32.sub (get_local $n) (i32.const 2)))
                     (call $fib (i32.sub (get_local $n) (i32.const 1))))))
)
