
fun PrimeNumberGenerator() : ArrayList<String> {

    val arrayListPrimeNumber = ArrayList<String>()

    for (num in 2..3400) { // init loop from 2..limit ex : 2..3 = 2,3
        var isPrime = true // need flag for return
        for (i in 2 until num) // next loop from 2 until num ex : 2 until 4 = 2,3 or 2 until 3 = 2
            if (num % i == 0) { // check prime ex : 4 % 2 == 0 !isPrime
                isPrime = false // set flag to false
                break // break read script , return to main loop
            }
        if (isPrime) // flagPrime true ?; !println
            arrayListPrimeNumber.add(num.toString()) //assign the value to an arrayList of prime
    //                println(num) // num
    }
    return arrayListPrimeNumber

}


fun main(args: Array<String>) {
    println(PrimeNumberGenerator().size)
}