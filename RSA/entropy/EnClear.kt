import kotlin.math.log2


fun main(args: Array<String>){

    // // experiment Entropy - cipherText
    val dataList = mutableListOf<Int>(
        57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 76, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41, 43, 57, 11, 133, 67, 11, 30, 136, 40, 102, 76, 114, 102, 88, 102, 41
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