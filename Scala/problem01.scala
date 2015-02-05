def problem1(limit: Int, factors: List[Int]) = {
  
  def cond(n: Int): Boolean = {
  	factors exists {n % _ == 0}
  }
  
  def allInts: Stream[Int] = (1 until limit).toStream
  def onlyMults: Stream[Int] = allInts filter cond
  
  onlyMults.sum
}
