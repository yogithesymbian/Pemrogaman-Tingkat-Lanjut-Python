package id.scode.informationdevice.key

import android.annotation.SuppressLint
import android.util.Log
import id.scode.informationdevice.*
import kotlinx.coroutines.delay
import java.text.SimpleDateFormat

/**
 * @Authors scodeid | Yogi Arif Widodo
 * Created on 31 12/31/19 7:42 PM 2019
 * id.scode.informationdevice.key
 * https://github.com/yogithesymbian
 * Android Studio 3.5.3
 * Build #AI-191.8026.42.35.6010548, built on November 15, 2019
 * JRE: 1.8.0_202-release-1483-b49-5587405 amd64
 * JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
 * Linux 5.3.0-kali3-amd64
 */
object ChoosePq {
    private val TAG_LOG = ChoosePq::class.simpleName
    /**
     * generate p number and q number
     * @see Map
     * @see Any
     * @param data
     * @throws Exception
     */
    @Throws(Exception::class)
    suspend fun mapPq(data: ArrayList<String>): Map<String, Any> {

        delay(1000L)
        Log.d(TAG_LOG, "result size prime number is ${data.size}")

        // init HashMap for assign the p and q
        val keyMap = HashMap<String, Any>(4)

        /**
         * DateTime
         * @suppress java.text.SimpleDateFormat
         */
        val currentTimeMillis = System.currentTimeMillis()
        @SuppressLint("SimpleDateFormat")
        val df = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        @SuppressLint("SimpleDateFormat")
        val dfDate = SimpleDateFormat("yyyy-MM-dd")
        @SuppressLint("SimpleDateFormat")
        val dfTime = SimpleDateFormat("HH:mm:ss")

        @SuppressLint("SimpleDateFormat")
        val dfSec = SimpleDateFormat("ss")
        @SuppressLint("SimpleDateFormat")
        val dfMin = SimpleDateFormat("mm")
        @SuppressLint("SimpleDateFormat")
        val dfHr = SimpleDateFormat("hh")

        val currentSec: String = dfSec.format(currentTimeMillis)
        val currentMin: String = dfMin.format(currentTimeMillis)
        val currentHr: String = dfHr.format(currentTimeMillis)
        val currentDf: String = df.format(currentTimeMillis)

        val currentDate: String = dfDate.format(currentTimeMillis)
        val currentTime: String = dfTime.format(currentTimeMillis)

        Log.d(
            TAG_LOG, """
            [*]
            ===========================================
                            TIME_INIT
            ===========================================
            default time : $currentTimeMillis
            waktu sekarang : $currentDf
            Hours : $currentHr
            Min : $currentMin
            Sec : $currentSec 
            ===========================================
                            TIME_INIT
            ===========================================
        """.trimIndent()
        )

        // get current time hour,min,sec
        val position1 = currentHr.toInt()
        val position2 = currentMin.toInt()
        val position3 = currentSec.toInt()

        val position4 = position2 + position3 // min + sec
        val position5 = position2 * position3 // min * sec
        val position6 = position1 * position2 // hr * min

        Log.d(
            TAG_LOG, """
            [*]
            ==============================================
            TIME POSITION
            ==============================================
            when position 1 < 2 3 4 5 6 use [ GMT+8 //DEFAULT ]
            1 = $position1  HOUR * 2
            1 < $position2  MIN
            1 < $position3  SEC
            1 < $position4  MIN + SEC
            1 < $position5  MIN * SEC
            1 < $position6  HR  * MIN
            ================================================
            INIT BEFORE SET DATA POSITION 
            FOR RESULT PRIME [ ARRAY LIST ] POSITION | TIME
            ================================================
        """.trimIndent()
        )
        /**
         * convert GMT+7
         */
        val differentTime = toGMTFormat(currentDate, currentTime)
        differentTime?.let {
            val getTimeGMT7 = dfTime.format(it)
            Log.d(TAG_LOG, "time GMT+7 $getTimeGMT7")
        }

        // assign the map with key [PRIME_NUM_P]
        keyMap[PRIME_NUM_P] = data[position1 * 2]
        Log.d(TAG_LOG, "timePosition P = $position1 * 2")
        keyMap[POSITION_P] = position1 * 2

        // assign the map with key [PRIME_NUM_Q]
        when { // these rule for data Q number
            position1 < position2 && position1 != position2 ->
                position2.let {
                    keyMap[PRIME_NUM_Q] = data[it]
                    Log.d(TAG_LOG, "timePosition Q = $it")
                    keyMap[POSITION_Q] = it
                }
            position1 < position3 && position1 != position3 ->
                position3.let {
                    keyMap[PRIME_NUM_Q] = data[it]
                    Log.d(TAG_LOG, "timePosition Q = $it")
                    keyMap[POSITION_Q] = it
                }
            position1 < position4 && position1 != position4 ->
                position4.let {
                    keyMap[PRIME_NUM_Q] = data[it]
                    Log.d(TAG_LOG, "timePosition Q = $it")
                    keyMap[POSITION_Q] = it
                }
            position1 < position5 && position1 != position5 ->
                position5.let {
                    keyMap[PRIME_NUM_Q] = data[it]
                    Log.d(TAG_LOG, "timePosition Q = $it")
                    keyMap[POSITION_Q] = it
                }
            position1 < position6 && position1 != position6 ->
                position6.let {
                    keyMap[PRIME_NUM_Q] = data[it]
                    Log.d(TAG_LOG, "timePosition Q = $it")
                    keyMap[POSITION_Q] = it
                }
        }
        return keyMap

    }

    /**
     * P Number
     * @return
     * @throws Exception
     */
    @Throws(Exception::class)
    fun getPrimeNumP(keyMap: Map<String, Any>): String {
        val key = keyMap[PRIME_NUM_P]
        Log.d(TAG_LOG, "number P : $key | where thePrime[timePosition]")
        return key.toString()
    }

    /**
     * Q Number
     * @return
     * @throws Exception
     */
    @Throws(Exception::class)
    fun getPrimeNumQ(keyMap: Map<String, Any>): String {
        val key = keyMap[PRIME_NUM_Q]
        Log.d(TAG_LOG, "number Q : $key | where thePrime[timePosition]")
        return key.toString()
    }


}