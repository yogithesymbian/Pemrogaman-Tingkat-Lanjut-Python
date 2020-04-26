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
    // val ePubKeyNya = "131"
    // val ePrivKey = "7931"
    // val nNumber = "9563"

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

    // PDATA 1 #
    // val ePubKeyNya = "1867"
    // val ePrivKey = "29203"
    // val nNumber = "237323"

    // PDATA 2
    // val ePubKeyNya = "191"
    // val ePrivKey = "38039"
    // val nNumber = "64241"

    // PDATA 3
    // val ePubKeyNya = "301"
    // val ePrivKey = "40333"
    // val nNumber = "73319"

    // PDATA 4
    // val ePubKeyNya = "551"
    // val ePrivKey = "7127"
    // val nNumber = "246749"

    // PDATA 5
    // val ePubKeyNya = "409"
    // val ePrivKey = "160865"
    // val nNumber = "219991"

    // PDATA 6
    // val ePubKeyNya = "101"
    // val ePrivKey = "6701"
    // val nNumber = "7373"

    // PDATA 7
    // val ePubKeyNya = "1489"
    // val ePrivKey = "43249"
    // val nNumber = "437537"

    // PDATA 8
    // val ePubKeyNya = "137"
    // val ePrivKey = "4073"
    // val nNumber = "6191"

    // PDATA 9
    // val ePubKeyNya = "387"
    // val ePrivKey = "18891"
    // val nNumber = "24523"

    // PDATA 10
    val ePubKeyNya = "193"
    val ePrivKey = "2257"
    val nNumber = "8159"

    // PDATA 11
    // val ePubKeyNya = "515"
    // val ePrivKey = "19115"
    // val nNumber = "31921"

    // PDATA 12
    // val ePubKeyNya = "667"
    // val ePrivKey = "1583"
    // val nNumber = "2893"


    // PDATA 13 | versi 2 | array.size - hh
    // val ePubKeyNya = "1813"
    // val ePrivKey = "187777"
    // val nNumber = "192989"

    println("""
    plainText : $plainText
    PublicKey : $ePubKeyNya
    PrivateKey: $ePrivKey
    (n)       : $nNumber
""".trimIndent()
)

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


    val arrayListAsciiBack = ArrayList<String>()

    for (i in 0 until  arrayListCipher.size){
        arrayListAsciiBack.add(arrayListCipher[i].toInt().toBigDecimal().pow(ePrivKey.toInt()).remainder(nNumber.toBigDecimal()).toString())
    }

//     println("""
//     [*]
//     ascii     : $arrayListAscii

//     cipher    : $arrayListCipher

//     asciiBack : $arrayListAsciiBack
// """.trimIndent()
// )


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