fun main(args: Array<String>) {

    val plainText = """
    Yogi Arif Widodo, [17.04.20 10:55]
    السلامعليكمورحمةاللهبركاته
    <!--
    (DOCUMENT~3986)
    Obat kehidupan adalah sederhana.
    Sederhana itu cara hidup.
    Cara hidup itu sederhana.-->
    """
    val ePubKeyNya = "131"
    val ePrivKey = "7931"
    val nNumber = "9563"

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

    println("""
    [*]
    polnes security
    PublicKey : $ePubKeyNya
    (n)       : $nNumber
    plainText : $plainText
    ascii     : $arrayListAscii

    cipher    : $arrayListCipher

    PrivateKey: $ePrivKey

    asciiBack : $arrayListAsciiBack
""".trimIndent()
)

    val arrayListAsciiBackChar = ArrayList<String>()
    // var test = ""
    for (i in 0 until  arrayListAsciiBack.size){
         arrayListAsciiBackChar.add(arrayListAsciiBack[i].toInt().toChar().toString())
        // println("${arrayListAsciiBack[i].toInt().toChar()}")
        // test = "${arrayListAsciiBack[i].toInt().toChar()}"
    }

    val hasilDekripsi = arrayListAsciiBackChar.joinToString(separator ="") { it }
    println(hasilDekripsi)

    val responseDekripsi = "data plainText dan hasil dekrips adalah sama : "

    if (plainText == hasilDekripsi)
        println("$responseDekripsi true")
    else
        println("$responseDekripsi false")
    // println(test)



}