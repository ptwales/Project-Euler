import scala.math.BigInt

object Main extends App {
  
  def gcd[T](a: T, b: T): T = {
    if(b == 0) a
    else gcd(b, a % b)
  }
  
  def lcm[T](a: T, b: T): T = {
    a * b / gcd(a, b)
  }
  
  def lcmm[T](xs: List[T]): T = {
    xs reduceLeft lcm
  }
  
  def problem5[T](rng: Range) = lcmm[T](rng.toList)
  
}
  
