fun GetDNumber() : Int? {

    var dNumber : Int? = null
    val resultNumberN = 9563
    val pubKey = 131
    val resultFaiN = 9360

    for (i in 0..resultNumberN.toInt()) {

        val dataPrivateKey: Int = (pubKey.toInt() * i) % resultFaiN.toInt()
        if (dataPrivateKey == 1)
            dNumber = i

    }

    return dNumber

}


fun main(args: Array<String>) {
    println("decrypt | private key : ${GetDNumber()}")
}