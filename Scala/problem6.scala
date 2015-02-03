object Main extends App {

  def offset[T](method: T => T)(lo: T = 1, hi: T)(implicit int: Integral[T]): T = {
    import int._
    method(hi) - method(lo - 1)
  }

  def gaussSum[T](n: T)(implicit int: Integral[T]): T = {
    import int._
    n*(n + 1)/2
  }
  
  def gaussSqrSum[T](n: T)(implicit int: Integral[T]): T = {
    import int._
    n*(2*n + 1)*(n + 1)/6
  }
  
  def problem6[T](n: T)(implicit int: Integral[T]): T = {
    val gsum = gaussSum(n)
    (gsum * gsum) - gaussSqrSum(n)
  }
  
}
