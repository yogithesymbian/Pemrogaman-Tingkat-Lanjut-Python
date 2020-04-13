fun main(args: Array<String>) {
    
    val plainText = "BUDI"
    val ePubKeyNya = "155"
    val nNumber = "3383"

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
            arrayListCipher.add("0${resultNya.toInt()}")
        else
            arrayListCipher.add("${resultNya.toInt()}")
    }



    val ePrivKey = "2003"

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
    // var test = ""
    for (i in 0 until  arrayListAsciiBack.size){
        println("${arrayListAsciiBack[i].toInt().toChar()}")
        // test = "${arrayListAsciiBack[i].toInt().toChar()}"
    }
    // println(test)
}