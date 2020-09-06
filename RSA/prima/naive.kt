fun isPrime(n: Int) : Boolean {
    // # Corner case
    if (n <= 1)
        return false

    // # Check from 2 to n-1
    for(i in 2..n){
        if (n % i == 0)
            return false
        else
            return true
    }
    return true
}

fun main() {
    // # Driver Program
    print(isPrime(11))
}