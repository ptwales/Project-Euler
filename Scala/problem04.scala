def isPalindrome(str: String): Boolean = {
  (str == str.reverse)
}
/*
 * abccba = a*10^5 + b*10^4 + c*10^3 + 100c + 10b + a
 *        = 100001a + 10010b + 1100c
 *        = 11(9091a + 910b + 100c)
 */
def palindromeRange(digitCount: Int): Range = {
  ???
}

def xDigitRange(digitCount: Int): Range = {
  def powerOfTen(n: Int): Int = scala.math.pow(10, n).toInt
  val lower: Int = powerOfTen(digitCount - 1)
  val upper: Int = powerOfTen(digitCount)
  (lower until upper)
}

def problem4(digitCount: Int): Int = {
  val rng = xDigitRange(digitCount).reverse
  lazy val allPalindromes = for {
    i <- rng
    j <- (i to rng.head)
    prod = i * j
    if isPalindrome(prod.toString)
  } yield prod
  allPalindromes.max
}

