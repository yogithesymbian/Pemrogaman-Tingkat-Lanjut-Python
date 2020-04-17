const val limitPrime = "Politeknik Negeri Samarinda Tahun 2020"

fun limitPrimeNumber() : Int{

    var theNumber = 0
    for (element in limitPrime){
        theNumber += element.toInt()
    }
    return theNumber

}

fun main(args: Array<String>) {
    println(limitPrimeNumber())
}