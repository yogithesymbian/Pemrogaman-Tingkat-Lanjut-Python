import kotlin.math.log2


fun main(args: Array<String>){

    // pembangkitan 1 - cipherText
    // val dataList = mutableListOf<Int>(
    //     927, 4926, 753, 4158, 640, 6844, 2858, 3900, 8619, 6917, 8222, 4571, 6924, 4158, 2206, 6844, 4158, 8222, 4158, 5348, 4158, 8619, 6844, 1163, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 1487, 927, 1000, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 6844, 6917, 640, 4571, 6844, 623, 4158, 2865, 4158, 6844, 8619, 6917, 8222, 4571, 6924, 1487, 927, 4783, 4158, 2865, 4158, 6844, 8619, 6917, 8222, 4571, 6924, 6844, 6917, 640, 4571, 6844, 1163, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 1487, 927, 6844, 6844, 6844, 6844
    //     )
    // pembangkitan 3 - cipherText
    // val dataList = mutableListOf<Int>(
    //     14223, 3544, 4973, 4783, 14013, 3457, 9994, 14405, 13954, 5704, 15508, 4500, 13887, 4783, 3265, 3457, 4783, 15508, 4783, 16221, 4783, 13954, 3457, 13666, 14405, 15508, 14405, 10871, 13954, 4783, 3265, 4783, 16313, 14223, 8632, 14405, 15508, 14405, 10871, 13954, 4783, 3265, 4783, 3457, 5704, 14013, 4500, 3457, 2119, 4783, 10871, 4783, 3457, 13954, 5704, 15508, 4500, 13887, 16313, 14223, 11825, 4783, 10871, 4783, 3457, 13954, 5704, 15508, 4500, 13887, 3457, 5704, 14013, 4500, 3457, 13666, 14405, 15508, 14405, 10871, 13954, 4783, 3265, 4783, 16313, 14223, 3457, 3457, 3457, 3457
    //     )
    // pembangkitan 4 - cipherText
    // val dataList = mutableListOf<Int>(
    //     7659, 1725, 1425, 2182, 1911, 10982, 3359, 7331, 7600, 9879, 3925, 12147, 831, 2182, 9584, 10982, 2182, 3925, 2182, 10362, 2182, 7600, 10982, 5793, 7331, 3925, 7331, 7453, 7600, 2182, 9584, 2182, 940, 7659, 33, 7331, 3925, 7331, 7453, 7600, 2182, 9584, 2182, 10982, 9879, 1911, 12147, 10982, 11183, 2182, 7453, 2182, 10982, 7600, 9879, 3925, 12147, 831, 940, 7659, 6700, 2182, 7453, 2182, 10982, 7600, 9879, 3925, 12147, 831, 10982, 9879, 1911, 12147, 10982, 5793, 7331, 3925, 7331, 7453, 7600, 2182, 9584, 2182, 940, 7659, 10982, 10982, 10982, 10982
    //     )
    // pembangkitan 5 - cipherText
    // val dataList = mutableListOf<Int>(
    //     2177, 1261, 6008, 3643, 1889, 32, 5032, 4435, 3847, 2863, 297, 6027, 3461, 3643, 1292, 32, 3643, 297, 3643, 2472, 3643, 3847, 32, 3267, 4435, 297, 4435, 4054, 3847, 3643, 1292, 3643, 2410, 2177, 4023, 4435, 297, 4435, 4054, 3847, 3643, 1292, 3643, 32, 2863, 1889, 6027, 32, 6009, 3643, 4054, 3643, 32, 3847, 2863, 297, 6027, 3461, 2410, 2177, 5977, 3643, 4054, 3643, 32, 3847, 2863, 297, 6027, 3461, 32, 2863, 1889, 6027, 32, 3267, 4435, 297, 4435, 4054, 3847, 3643, 1292, 3643, 2410, 2177, 32, 32, 32, 32
    //     )

    // experiment Increase Entropy 5 - cipherText
    val dataList = mutableListOf<Int>(
        927, 6844, 6844, 6844, 6844, 4019, 4434, 9142, 6917, 6844, 8842, 2865, 6917, 5211, 6844, 4803, 6917, 8222, 4434, 8222, 4434, 4498, 6844, 3759, 5551, 5950, 1487, 8956, 445, 1487, 4897, 8956, 6844, 5551, 8956, 2940, 2018, 2018, 7691, 927, 6844, 6844, 6844, 6844, 2623, 1866, 5779, 1866, 2623, 1605, 5654, 1866, 2265, 7105, 1605, 1346, 1978, 926, 1605, 6031, 2623, 1866, 1866, 1607, 2100, 1978, 7105, 2623, 7342, 1607, 927, 6844, 6844, 6844, 6844, 4121, 1212, 5809, 5809, 927, 6844, 6844, 6844, 6844, 8424, 2688, 4926, 4783, 609, 732, 8977, 7021, 3490, 2091, 8697, 5690, 9095, 4246, 2792, 927, 6844, 6844, 6844, 6844, 4926, 753, 4158, 640, 6844, 2858, 3900, 8619, 6917, 8222, 4571, 6924, 4158, 2206, 6844, 4158, 8222, 4158, 5348, 4158, 8619, 6844, 1163, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 1487, 927, 6844, 6844, 6844, 6844, 1000, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 6844, 6917, 640, 4571, 6844, 623, 4158, 2865, 4158, 6844, 8619, 6917, 8222, 4571, 6924, 1487, 927, 6844, 6844, 6844, 6844, 4783, 4158, 2865, 4158, 6844, 8619, 6917, 8222, 4571, 6924, 6844, 6917, 640, 4571, 6844, 1163, 3900, 8222, 3900, 2865, 8619, 4158, 2206, 4158, 1487, 5809, 5809, 6219, 927, 6844, 6844, 6844, 6844
        )

    val counterData = dataList
                    .groupingBy { it }      // grouping data
                    .eachCount()        // probabilitas data
                    .filter {       // filter data | optional
                        it.value > 0
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
}