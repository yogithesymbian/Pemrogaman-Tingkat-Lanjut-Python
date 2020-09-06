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
    // val plainText = """
    // ```Yogi Arif Widodo, [17.04.20 10:55]```
    // *assalamu'alaikum warrahmatullahi wabarakatuh*
    // <!--
    // (CATATANBIASA~3986)
    // Obat kehidupan adalah sederhana.
    // Sederhana itu cara hidup.
    // Cara hidup itu sederhana. #simpel-->
    // """
//     val plainText = """
// “Ketahuilah, bahwa sesungguhnya kehidupan dunia ini hanyalah permainan dan suatu yang melalaikan, perhiasan dan bermegah-megah antara kamu serta berbangga-banggaan tentang banyaknya harta dan anak, seperti hujan yang tanam-tanamannya mengagumkan para petani; kemudian tanaman itu menjadi kering dan kamu lihat warnanya kuning kemudian menjadi hancur. Dan di akhirat (nanti) ada azab yang keras dan ampunan dari Allah serta keridhaan-Nya. Dan kehidupan dunia ini tidak lain hanyalah kesenangan yang menipu.”
//     """
//         val plainText = """
// "Know, that truly the life of this world is only a game and a neglect, adornment and boasting among you and boasting about the abundance of wealth and children, like rain whose crops amaze the peasants; Then the plant dries up and you see it is yellow and then crumbles. And in the hereafter (later) there will be harsh punishment and forgiveness from Allah and His good pleasure. And the life of this world is nothing but deceptive pleasures. "
//     """
//         val plainText = """
// Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda. Politeknik Samarinda.Politeknik Samarinda.Politeknik Samarinda.Politeknik Samarinda.
//         """
    val plainText = """
jika menggunakan simbol !@#$%^&*()_+{}:"><[];',/|~` apakah memiliki has1l perbandingan sama atau berbeda, belum diketahui karena sedang dicoba dan lihatlah disamping ini hasilnya jika menggunakan simbol ! dikeyboard sampai simbol ? dengan berdasarkan informasi peranti waktu yang digunakan dalam penentuan p dan q yang detailnya ada pada tahapan sebelumnya, ok! nb: fokus analisanya ada pada nilai keacakan data yang menggunakan shannon enteropi
    """

    // println("length plainText : ${plainText.length}")
    // P1
    val ePubKeyNya = "137"
    val ePrivKey = "22073"
    val nNumber = "36391"

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
    // val ePubKeyNya = "193"
    // val ePrivKey = "2257"
    // val nNumber = "8159"

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
    jml karakter : ${plainText.length}
    PublicKey : $ePubKeyNya
    PrivateKey: $ePrivKey
    (n)       : $nNumber
""".trimIndent()
)

    val arrayListAscii = ArrayList<String>()
    val arrayListCipher = ArrayList<String>()
    // val arrayListCipher = mutableListOf(
    //     22295, 190072, 190072, 190072, 190072, 69198, 69198, 69198, 185514, 145416, 99917, 55244, 190072, 54735, 20003, 55244, 118763, 190072, 66278, 55244, 120350, 145416, 120350, 145416, 146586, 190072, 182343, 56057, 148977, 40848, 117307, 1928, 40848, 85252, 117307, 190072, 56057, 117307, 85608, 147871, 147871, 60706, 69198, 69198, 69198, 22295, 190072, 190072, 190072, 190072, 161986, 127000, 43730, 43730, 127000, 107859, 127000, 130918, 171866, 79162, 127000, 107859, 127000, 55244, 60667, 171866, 130918, 190072, 52452, 127000, 20003, 20003, 127000, 152609, 130918, 127000, 120101, 171866, 107859, 107859, 127000, 152609, 55244, 190072, 52452, 127000, 30723, 127000, 20003, 127000, 60667, 127000, 120101, 171866, 152609, 161986, 22295, 190072, 190072, 190072, 190072, 133459, 17216, 7351, 7351, 22295, 190072, 190072, 190072, 190072, 82850, 16002, 54735, 106795, 54735, 106795, 54735, 17273, 115895, 59850, 54735, 120571, 54735, 40782, 129374, 35731, 69159, 94585, 108904, 22295, 190072, 190072, 190072, 190072, 22141, 30723, 127000, 120101, 190072, 60667, 191250, 152609, 55244, 120350, 171866, 26980, 127000, 48131, 190072, 127000, 120350, 127000, 107859, 127000, 152609, 190072, 43730, 191250, 120350, 191250, 20003, 152609, 127000, 48131, 127000, 40848, 22295, 190072, 190072, 190072, 190072, 120571, 191250, 120350, 191250, 20003, 152609, 127000, 48131, 127000, 190072, 55244, 120101, 171866, 190072, 17006, 127000, 20003, 127000, 190072, 152609, 55244, 120350, 171866, 26980, 40848, 22295, 190072, 190072, 190072, 190072, 16002, 127000, 20003, 127000, 190072, 152609, 55244, 120350, 171866, 26980, 190072, 55244, 120101, 171866, 190072, 43730, 191250, 120350, 191250, 20003, 152609, 127000, 48131, 127000, 40848, 190072, 147348, 43730, 55244, 130918, 26980, 191250, 107859, 7351, 7351, 161118, 22295, 190072, 190072, 190072, 190072
    // )

    // enkripsi
    for (element in plainText) {
        if (element.toInt() <= 99) // plainText (character) ke ascii code
            arrayListAscii.add("0${element.toInt()}")
        else
            arrayListAscii.add("${element.toInt()}")
        // ascii code ke blockcipher
        val resultNya = element.toInt().toBigDecimal().pow(ePubKeyNya.toInt())
            .remainder(nNumber.toBigDecimal())
        // masukan hasil ke array list cipher
        if (resultNya.toInt() <= 999) // assign fill 0
            arrayListCipher.add("${resultNya.toInt()}")
        else
            arrayListCipher.add("${resultNya.toInt()}")
    }


    val arrayListAsciiBack = ArrayList<String>()

    // dekripsi blockcipher to ascii code
    for (i in 0 until  arrayListCipher.size){
        arrayListAsciiBack.add(arrayListCipher[i].toInt().toBigDecimal().pow(ePrivKey.toInt()).remainder(nNumber.toBigDecimal()).toString())
    }

    // cipher to ASCII
    val arrayListCipherToChar = ArrayList<String>()
    for (i in 0 until  arrayListCipher.size){
         arrayListCipherToChar.add(arrayListCipher[i].toInt().toChar().toString())
    }
    val hasilCipherToAscii = arrayListCipherToChar.joinToString(separator ="") { it }

// Οዌዌዌᅒ⎶ᬅ⊊଱ᬅᑛዃᬅ„ᅒ„ᅒᆒຯᖯ᜾׏⋼ƽ׏ጡ⋼ᖯ
// ⋼୼ߢߢḋዌዌዌΟтҋҋᓤᶘᇛ᫃ᓤᬅପᇛᶘ଱଱↫ᶘʀᇛᓤ
// ᓤ↫ᬅ˱଱ପʀᇛ↫тΟမҼᚱᚱΟኯ⊊ජ⊊ජ⊊ǋI⊊Ϩ⊊⇹ᘺ
// ⎇႖૨Οጾ˱ʀପ༼↫ᬅ„ᇛᬌ࢞„ᓤ↫ҋ༼„༼଱↫࢞׏ΟϨ༼„
// ༼଱↫࢞ᬅʀᇛɯ଱↫ᬅ„ᇛᬌ׏Οኯ଱↫ᬅ„ᇛᬌᬅʀᇛ
// ҋ༼„༼଱↫࢞׏ᒛҋᬅᶘᬌ༼ᓤᚱᚱᡋΟ


    println("""
    [*]
    ascii     : $arrayListAscii

    cipher    : $arrayListCipher

    cipherAscii : $hasilCipherToAscii

    asciiBack : $arrayListAsciiBack
""".trimIndent()
)
    // ascii code to character (plainText)
    val arrayListAsciiBackChar = ArrayList<String>()
    // var test = ""
    for (i in 0 until  arrayListAsciiBack.size){
         arrayListAsciiBackChar.add(arrayListAsciiBack[i].toInt().toChar().toString())
        // println("${arrayListAsciiBack[i].toInt().toChar()}")
        // test = "${arrayListAsciiBack[i].toInt().toChar()}"
    }
    val responseDekripsi = "data plainText dan hasil dekripsi adalah sama : "

    val hasilDekripsi = arrayListAsciiBackChar.joinToString(separator ="") { it }
    println("\nhasil dekripsi \n $hasilDekripsi")

    if (plainText == hasilDekripsi && plainText.length == hasilDekripsi.length)
        println("$responseDekripsi true")
    else
        println("$responseDekripsi false")


}