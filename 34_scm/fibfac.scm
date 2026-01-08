#lang racket

;;let n be the number to be factorialed
(define (fact n)
  (cond
    [(equal? n 0) 1]
    [(* n (fact (- n 1)))]
    )
  )

;;let n be the place within the sequence
(define (fib n)
   (cond
    [(<= n 0) 0]
    [(= n 1) 1]
    [(+ (fib (- n 2)) (fib (- n 1)))]
    )
  )

;;test cases
(fact 3)
(fib 6)