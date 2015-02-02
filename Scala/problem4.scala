def isPalindrome(str: String): Boolean = {
  (str == str.reverse)
}

def xDigitRange(digitCount: Int): Range = {
  def powerOfTen(n: Int): Int = scala.math.pow(10, n).toInt
	val lower: Int = powerOfTen(digitCount - 1)
	val upper: Int = powerOfTen(digitCount)
	(lower until upper)
}

def problem4(digitCount: Int): Int = {
  val rng = xDigitRange(digitCount)
  lazy val allPalindromes = for {
    i <- rng.reverse
    j <- (i to rng.head by -1)
    prod = i * j
    if isPalindrome(prod.toString)
  } yield prod
  allPalindromes.head
}
