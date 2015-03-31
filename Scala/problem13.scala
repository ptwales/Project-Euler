import scala.math.BigInt // Cheating, write your own!

val bigints: List[String] = scala.io.Source.fromFile("../txt/problem13.txt").mkString.split("\n")

def problem13(nums: List[String], digitCount: Int): String = {
  
  def bigInts: Stream[BigInt] = nums.toStream.map(BigInt(_))
  val sum: BigInt = bigInts.sum
  
  sum.toString take digitCount
}
