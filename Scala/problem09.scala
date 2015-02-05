def sqr(y: Double): Double = {
  scala.math.pow(y, 2)
}
	
def problem9(x: Int): Option[Int] = {
  val sqrx = sqr(x) // let in
  def fb(a: Double): Double = (sqrx - 2*x*a)/(2*(x-a))
  def fc(a: Double, b: Double): Double = scala.math.sqrt(sqr(a) + sqr(b))
  // use streams with filters and find instead
  val solution = (for {
    a <- (1 to x/3)
    val b: Double = fb(a.toDouble)
    if b.isWhole
    val c: Double = fc(a.toDouble, b.toDouble)
    if c.isWhole
  } yield (a * b * c).toInt ).headOption
  
  solution
}
