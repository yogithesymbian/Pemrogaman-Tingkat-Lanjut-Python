

// main function
fun main() {
    
    val hasil = "3048"
    val angka = "85"
    // kunci
    // moodulus

    val arrayList = ArrayList<Int>()
    try {
        for (i in 1..100){
            var a = i
            for (j in 1..5000){
                if (angka.toInt().toBigDecimal().pow(i).remainder(j.toBigDecimal()).toString() == hasil){
                    arrayList.add(a)
                    println("no $a angka $angka [const] ,  key $i dan modulus $j menghasilkan $hasil")
                }
            }
        }
    } catch (e: ArithmeticException){
        println("error $e")
    }
    println("banyak key dan modulus yang menghasilkan 795 dari plainTextAscii '66' adalah ${arrayList.size} key")

}