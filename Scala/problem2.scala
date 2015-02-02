val fibs:Stream[Int] = 0 #:: 1 #:: fibs.zip(fibs.tail).map { n => n._1 + n._2 }

def problem2(limit: Int): Int = {
	val fibPart = fibs takeWhile { _ < limit }
	val fibFilt = fibPart filter { _ % 2 == 0 } 
  fibFilt.sum
}
