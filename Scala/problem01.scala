def problem1(limit: Int, factors: List[Int]): Int = {
  
  def cond(n: Int): Boolean = {
    factors.exists(x => n % x == 0})
  }
  def allInts: Stream[Int] = {
    1.until(limit).toStream
  }
  def onlyMults: Stream[Int] = {
    allInts.filter(cond)
  }
  
  onlyMults.sum
}
