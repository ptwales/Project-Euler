lazy val trianglularNumbers: Stream[Int] = Stream.from(2).scanLeft(1)(_ + _)

def factors(n: Int): List[Int] = {
}

def problem12(factCount: Int): Int = {
  trianglularNumbers.map(factors).find(_.count = 5)
}
