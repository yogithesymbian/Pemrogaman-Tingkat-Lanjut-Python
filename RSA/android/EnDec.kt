fun main(args: Array<String>) {

    // val plainText = """
    // Yogi Arif Widodo, [17.04.20 10:55]
    // السلامعليكمورحمةاللهبركاته
    // <!--
    // (DOCUMENT~3986)
    // Obat kehidupan adalah sederhana.
    // Sederhana itu cara hidup.
    // Cara hidup itu sederhana.-->
    // """
    val plainText = """
    ```Yogi Arif Widodo, [17.04.20 10:55]```
    *assalamu'alaikum warrahmatullahi wabarakatuh*
    <!--
    (CATATANBIASA~3986)
    Obat kehidupan adalah sederhana.
    Sederhana itu cara hidup.
    Cara hidup itu sederhana. #simpel-->
    """
    // println("length plainText : ${plainText.length}")
    // P1
    val ePubKeyNya = "131"
    val ePrivKey = "7931"
    val nNumber = "9563"

    // P2
    // val ePubKeyNya = "227"
    // val ePrivKey = "383"
    // val nNumber = "12737"

    // P3
    // val ePubKeyNya = "109"
    // val ePrivKey = "2949"
    // val nNumber = "16351"

    // P4
    // val ePubKeyNya = "173"
    // val ePrivKey = "5309"
    // val nNumber = "13199"

    // P5
    // val ePubKeyNya = "197"
    // val ePrivKey = "1373"
    // val nNumber = "6107"

    val arrayListAscii = ArrayList<String>()
    val arrayListCipher = ArrayList<String>()

    for (element in plainText) {
        if (element.toInt() <= 99)
            arrayListAscii.add("0${element.toInt()}")
        else
            arrayListAscii.add("${element.toInt()}")

        val resultNya = element.toInt().toBigDecimal().pow(ePubKeyNya.toInt())
            .remainder(nNumber.toBigDecimal())

        if (resultNya.toInt() <= 999)
            arrayListCipher.add("${resultNya.toInt()}")
        else
            arrayListCipher.add("${resultNya.toInt()}")
    }


    val arrayListAsciiBack = ArrayList<String>()

    for (i in 0 until  arrayListCipher.size){
        arrayListAsciiBack.add(arrayListCipher[i].toInt().toBigDecimal().pow(ePrivKey.toInt()).remainder(nNumber.toBigDecimal()).toString())
    }

//     println("""
//     [*]
//     polnes security
//     PublicKey : $ePubKeyNya
//     (n)       : $nNumber
//     plainText : $plainText
//     ascii     : $arrayListAscii

//     cipher    : $arrayListCipher

//     PrivateKey: $ePrivKey

//     asciiBack : $arrayListAsciiBack
// """.trimIndent()
// )
    println("""
    plainText : $plainText
    PrivateKey: $ePrivKey
    (n)       : $nNumber
""".trimIndent()
)

    val arrayListAsciiBackChar = ArrayList<String>()
    // var test = ""
    for (i in 0 until  arrayListAsciiBack.size){
         arrayListAsciiBackChar.add(arrayListAsciiBack[i].toInt().toChar().toString())
        // println("${arrayListAsciiBack[i].toInt().toChar()}")
        // test = "${arrayListAsciiBack[i].toInt().toChar()}"
    }
    val responseDekripsi = "data plainText dan hasil dekripsi adalah sama : "

    val hasilDekripsi = arrayListAsciiBackChar.joinToString(separator ="") { it }
    println("hasil dekripsi \n $hasilDekripsi")

    if (plainText == hasilDekripsi && plainText.length == hasilDekripsi.length)
        println("$responseDekripsi true")
    else
        println("$responseDekripsi false")


}