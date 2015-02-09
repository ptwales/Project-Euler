
def isEven(n: Int): Boolean = {
  (n % 2) == 0
}


def collatz(n: Int): Stream[Int] = {
  
  def collatzNext(n: Int) = {
    if (isEven(n)) n/2
    else 3*n + 1
  }
  
  if (n > 1) n #:: collatz(collatzNext(n))
  else Stream[Int]()
}

def problem14(limit: Int): Int = {
  
  def newValues(cs: Stream[Int], sols: Map[Int, Int]): List[Int] = {
    
    def isNewVal(n: Int): Boolean = !sols.contains(n)
    // DOESN'T INCLUDE THE NEXT VALUE!
    cs.takeWhile(isNewVal).toList
  }
  
  def newAnswers(cs: List[Int], sols: Map[Int, Int]): Map[Int, Int] = {
    
    lazy val addLen: Int = sols(cs.last)
    def withCounts: List[Int] = cs.reverse.zipWithIndex.tail
    
    withCounts.map(t => (t._1, t._2 + addLen)).toMap
  }
  
  lazy val solutions = scala.collection.mutable.Map[Int, Int](1 -> 1)
  for (n <- (2 until limit)) {
    solutions ++= newAnswers(newValues(collatz(n), solutions), solutions)
  }
  
  solution.maxBy(_._2)._1
}
