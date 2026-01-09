//Team Virginia :: Veronika Duvanova, Ashley Li
//SoftDev pd5
//K35 - Basic functions in JavaScript
//2026-01-09f

//JavaScript implementations of recursive Scheme functions

//factorial:
define fact(n) {
  if (n == 0) {
    return(0);
  } else {
    return(n * fact(n - 1));
  }
};
//<your team's fact(n) implementation>

//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)
console.log(fact(3));

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
define fib(n) {
  if (n == 0) {
    return(0);
  } else {
    return(
      fin (n - 1) + fib(n - !));
  }
};
//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
