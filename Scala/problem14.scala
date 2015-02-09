
def isEven(n: Int): Boolean = {
  (n % 2) == 0
}

class CollatzSequence(initial: Int) {
  
  def next(n: Int): Int = {
    if(isEven(n)) n/2
    else 3*n + 1
  }
  
  lazy val sequence: Stream[Int] = {
    if (initial > 1) intial #:: CollatzSequence(next(initial)).sequence
    else Stream(initial)
  }
  
  lazy val newValues(knownVals: Set[Int] = Set(1)): List[CollatzSequence] = {
    def isNew(cs: CollatzSequence): Boolean = !knownVals.contains(cs.initial)
    sequence.takeWhile(isNew)
  }
  
  lazy val newSolutions(knownLengths: Map[Int, Int] = Map(1 -> 1)) = {
    // newValues(knownLengths.keys.toSet)
  }
  
  lazy val length(knownLengths: Map[Int,Int] = Map(1 -> 1)) = {
    
  }
  
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
