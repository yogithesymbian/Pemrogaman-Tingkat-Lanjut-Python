import kotlin.math.pow

fun main() {

    val a = 66
    val b = 79
    val bagi = 3337

    val pow = a.toDouble().pow(b.toDouble())
    val mod0 = pow % 3337
    val mod1 = Math.floorMod(pow.toInt(),bagi)
    val mod2 = pow.toLong() % 3337
    val mod3 = pow.toBigDecimal().remainder(bagi.toBigDecimal())
    val mod4 = 66.0.pow(79) % 3337

//    val mod5 = pow.toBigDecimal()

    println("""
        [*]
        ========================
                x^y | $a^$b
        ========================
        A.1 ( $a ^ $b ) = $pow   //normal 
        A.2 ( $a ^ $b ) = ${pow.toInt()}              //toInt()
        A.3 ( $a ^ $b ) = ${pow.toLong()}    //toLong
        A.4 ( $a ^ $b ) = ${pow.toBigDecimal()}//toBigDecimal
        _________________________________________________________
        
        B.1 $pow mod $bagi = $mod0
        B.2 ${pow.toInt()} mod $bagi = $mod1
        B.3 ${pow.toLong()} mod $bagi = $mod2
        B.4 ${pow.toBigDecimal()} mod $bagi = $mod3
        
        directly $a.0 ^ $b.0 % $bagi = $mod4

    """.trimIndent())


    val data1 = 66
    val data2 = 79
    val modulus = 3337
    val result1 = data1.toBigDecimal().pow(data2).remainder(modulus.toBigDecimal())

    val init1 = data1.toBigDecimal()
    val init2 = modulus.toBigDecimal()

    val init3 = data1.toBigDecimal().pow(data2)
    val init4 = data1.toDouble().pow(data2)
    val init5 = data1.toFloat().pow(data2)

    println("""
        [*]
        $result1
        $init1
        $init2
        $init3
        $init4
        $init5
    """.trimIndent())
}