;; Taken from:
;;
;; https://github.com/WebAssembly/testsuite/blob/master/globals.wast
(module
  (import "test" "global0" (global i32))

  (global $a i32 (i32.const -2))
  (global (;1;) f32 (f32.const -3))
  (global (;2;) f64 (f64.const -4))
  (global $b i64 (i64.const -5))

  (global $x (mut i32) (i32.const -12))
  (global (;5;) (mut f32) (f32.const -13))
  (global (;6;) (mut f64) (f64.const -14))
  (global $y (mut i64) (i64.const -15))

  (global $z (mut i32) (global.get 0))
)
