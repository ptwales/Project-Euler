object Main extends App {

  def offset(method: Int => Int): Int = {
    (lo: Int, hi: Int) => method(hi) - method(lo - 1)
  }

  def gaussSum(n: Int): Int = n*(n + 1)/2
  def gaussSqrSum(n: Int): Int = n*(2*n+1)*(n+1)/6
  
}
