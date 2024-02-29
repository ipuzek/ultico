# palindRom

library(stringi)

jest_palindrom <- function(x) x == stringi::stri_reverse(x)

jest_palindrom("anA")

stringi::stri_reverse()