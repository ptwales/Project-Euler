
def isEven(n: Int): Boolean = {
  (n % 2) == 0
}

type CollatzSeq = Stream[Int]
def collatz(n: Int): CollatzSeq = {
  
  def collatzNext(n: Int) = {
    if (isEven(n)) n/2
    else 3*n + 1
  }
  
  if (n > 1) n #:: collatz(collatzNext(n))
  else Stream[Int]()
}

def problem14(limit: Int): Int = {
  
  type Answers = Map[Int, Int]

  /*
   * Calculates the length of a collatz sequence given
   * a map of known solutions
   */ 
  def collatzLength(cs: CollatzSeq, sols: Answers): Int = {
    
    def isSolved(n: Int): Boolean = sols.contains(n)
    lazy val solvedTilLength: Int = cs.indexWhere(isSolved) + 1
    
    if (solvedTilLength == 0) cs.length // sequence is already solved
    else {
      lazy val lastSolvedVal: Int = cs.take(solvedTilLength).last
      solvedTilLength + sols(lastSolvedVal)
    }
  }
  
  def addSolution(n: Int, sols: Answers): Answers = {
    lazy val len: Int = collatzLength(collatz(n), sols)
    sols + (n -> len)
  }
  
  def buildSolution(n: Int, sols: Answers): Answers = {
    if (n == limit) sols
    else {
      lazy val newSols: Answers = addSolution(n, sols)
      buildSolution(n+1, newSols)
    }
  }
  
  lazy val solution: Answers =  buildSolution(1, Map[Int, Int]())
  solution.maxBy(_._2)._1
}
