import kotlin.math.log2


fun main(args: Array<String>){

    // // experiment Entropy - cipherText
    val dataList = mutableListOf<Int>(
        10, 32, 32, 32, 32, 96, 96, 96, 89, 111, 103, 105, 32, 65, 114, 105, 102, 32, 87, 105, 100, 111, 100, 111, 44, 32, 91, 49, 55, 46, 48, 52, 46, 50, 48, 32, 49, 48, 58, 53, 53, 93, 96, 96, 96, 10, 32, 32, 32, 32, 42, 97, 115, 115, 97, 108, 97, 109, 117, 39, 97, 108, 97, 105, 107, 117, 109, 32, 119, 97, 114, 114, 97, 104, 109, 97, 116, 117, 108, 108, 97, 104, 105, 32, 119, 97, 98, 97, 114, 97, 107, 97, 116, 117, 104, 42, 10, 32, 32, 32, 32, 60, 33, 45, 45, 10, 32, 32, 32, 32, 40, 67, 65, 84, 65, 84, 65, 78, 66, 73, 65, 83, 65, 126, 51, 57, 56, 54, 41, 10, 32, 32, 32, 32, 79, 98, 97, 116, 32, 107, 101, 104, 105, 100, 117, 112, 97, 110, 32, 97, 100, 97, 108, 97, 104, 32, 115, 101, 100, 101, 114, 104, 97, 110, 97, 46, 10, 32, 32, 32, 32, 83, 101, 100, 101, 114, 104, 97, 110, 97, 32, 105, 116, 117, 32, 99, 97, 114, 97, 32, 104, 105, 100, 117, 112, 46, 10, 32, 32, 32, 32, 67, 97, 114, 97, 32, 104, 105, 100, 117, 112, 32, 105, 116, 117, 32, 115, 101, 100, 101, 114, 104, 97, 110, 97, 46, 32, 35, 115, 105, 109, 112, 101, 108, 45, 45, 62, 10, 32, 32, 32, 32
        )

    val counterData = dataList
                    .groupingBy { it }      // grouping data
                    .eachCount()        // probabilitas data
                    .filter {       // filter data | optional
                        it.value >= 0
                    }
    val counterDataValue = counterData.values       // ambil value

    // check initialize
    println("""
    listData : $dataList

    listData Size ${dataList.size}

    counterData : $counterData

    counterData Values : $counterDataValue

    CounterData Value Size ${counterDataValue.size}
    """.trimIndent())

    var entropy = 0.0 // initialize entopy

    for (count in counterDataValue){ // loop for probability data value
        // println(count)
        var pX = count.toDouble() / dataList.size
        // println(pX)
        entropy += - pX * log2(pX)      // formula entropy
        // println(entropy)
    }
    println("entropy : $entropy")
    println("debug")
}