import scala.math.BigInt

object Main extends App {

  def offset(method: BigInt => BigInt)(lo: BigInt = 1, hi: BigInt): BigInt = {
    method(hi) - method(lo - 1)
  }
  
  def gaussSum(n: BigInt): BigInt = {
    n*(n + 1)/2
  }
  
  def gaussSqrSum(n: BigInt): BigInt = {
    n*(2*n + 1)*(n + 1)/6
  }
  
  def problem6(n: BigInt): BigInt = {
    val gsum = gaussSum(n)
    (gsum * gsum) - gaussSqrSum(n)
  }

}
