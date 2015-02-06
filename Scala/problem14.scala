
def isEven(n: Int): Boolean = {
  (n % 2) == 0
}

def isOdd(n: Int): Boolean = !isEven(n)

def collatz(n: Int): Stream[Int] = {
  
  def collatzNext(n: Int) = {
    if (isEven(n)) n/2
    else 3*n + 1
  }
  
  n #:: collatz(collatzNext(n))
}

def problem14(limit: Int): Int = {

  val domain: Stream[Int] = (1 until limit).toStream
  val indexedCollatz = domain map {x => (x, collatz(x))}
  val indexedLengths = indexedCollatz map {t => (t._1, t._2.length)}
  
  (indexedLengths maxBy _._2)._1
}
