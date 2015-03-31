import collection.breakOut

def readTriangle(trianlge: String): List[Vector[Int]] = {

  lazy val rows = trianlge.split("\n").toList
  
  def readRow(row: String): Vector[Int] = {
    lazy val nums = row.split(" ").map(_.toInt)
    nums.to[Vector]
  }
  
  rows.map(readRow)
}

def problem14(triangle: List[Vector[Int]]): Int = {

  def condenseRows(smallRow: Vector[Int], bigRow: Vector[Int]): Vector[Int] = {
    
    lazy val options = bigRow.sliding(2).toStream
    lazy val optimal = options.map(_.max)
    
    (smallRow, optimal).zipped.map(_ + _)
  }
  
  triangle.reduceRight(condenseRows)
}
