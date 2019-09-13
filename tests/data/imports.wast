;; Taken from:
;;
;; https://github.com/WebAssembly/testsuite/blob/master/imports.wast
(module
  ;; Functions
  (import "test" "func0" (func))
  (import "test" "func1" (func (param i32)))
  (import "test" "func2" (func (param f32)))
  (import "test" "func3" (func (result i32)))
  (import "test" "func4" (func (result f32)))
  (import "test" "func5" (func (param i32) (result i32)))
  (import "test" "func6" (func (param i64) (result i64)))

  ;; Tables
  (import "test" "table" (table 10 20 funcref))

  ;; Memories
  (import "test" "memory" (memory 1 2))

  ;; Globals
  (import "test" "global0" (global i32))
  (import "test" "global1" (global i64))
  (import "test" "global2" (global f32))
  (import "test" "global3" (global f64))
)
