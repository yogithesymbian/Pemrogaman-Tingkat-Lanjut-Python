package id.scode.informationdevice.key

import android.util.Log
import id.scode.informationdevice.limitPrime
import id.scode.informationdevice.limitPrimeNumber
import kotlinx.coroutines.delay
import java.lang.ArithmeticException

/**
 * @Authors scodeid | Yogi Arif Widodo
 * Created on 31 12/31/19 4:31 PM 2019
 * id.scode.informationdevice.key
 * https://github.com/yogithesymbian
 * Android Studio 3.5.3
 * Build #AI-191.8026.42.35.6010548, built on November 15, 2019
 * JRE: 1.8.0_202-release-1483-b49-5587405 amd64
 * JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
 * Linux 5.3.0-kali3-amd64
 */
object PrimeNumberGenerate {
    /**
     * initialize
     * @see Int()
     * @see ArrayList with Int type of casting the value
     * for prime number
     */
    private val arrayListPrimeNumber = ArrayList<String>()
    private val TAG_LOG = PrimeNumberGenerate::class.simpleName
    /**
     * generate prime number
     * @return
     * @throws Exception
     */
    @Throws(Exception::class)
    suspend fun generatePrimeNumber(): ArrayList<String> {

        delay(1000L)
        try {

            for (num in 2..limitPrimeNumber()) { // init loop from 2..limit ex : 2..3 = 2,3
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
//            println(arrayListPrimeNumber)
        } catch (e: ArithmeticException) {
            println(e.printStackTrace().toString())
        }
        limitPrimeNumber().also {

        }
        Log.d(
            TAG_LOG, """
            [*]
            ascii decimal "$limitPrime is ${limitPrimeNumber()}
            range prime number is 2 until ${limitPrimeNumber()}
        """.trimIndent()
        )
        return arrayListPrimeNumber
    }
}