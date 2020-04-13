
// 6 line + readable style [1]
for (num in 1..10 + 1)
    if (num > 1){
        for (i in 2..num)
            if (num % 1 == 0) break
        println(num)
    }
// 6 line + readable style [1]
for (num in 1..10 + 1)
    if (num == 1) println("skip")
    else {
        for (i in 2..num) if (num % 1 == 0) break
        println(num)
    }











        // 8 Line + readable
        for (num in 1..10 + 1)
            when(num){
                1 -> println("skip")
                else -> {
                    for (i in 2..num) if (num % 1 == 0) break
                    println(num)
                }
            }
        // 8 Line + readable
        for (num in 1..10 + 1)
            when {
                num > 1 -> {
                    for (i in 2..num)
                        if (num % 1 == 0) break
                    println(num)
                }
            }
        // 5 Line + readable
        for (num in 1..10 + 1)
            if (num != 1) {
                for (i in 2..num) if (num % 1 == 0) break
                println(num)
            } else println("skip")