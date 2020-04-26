
fun main(){

    var dataGMTList = mutableListOf<Int>()
    var dataGMTListInFiveMin = mutableListOf<Int>()

    for (i in 0..23){
        dataGMTList.add(i)
    }
    // println(dataGMTList.random())
    for (i in 0..12){
        dataGMTListInFiveMin.add(dataGMTList.random()) // add rand IntNsum
    }

    println(dataGMTListInFiveMin)

    // val stateZoneTime = (1 until listZoneTime.size).random() // for flag state choose gmt
}