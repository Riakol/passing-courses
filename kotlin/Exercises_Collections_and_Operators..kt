package org.example

import java.util.LinkedList
import java.util.Queue
import kotlin.time.measureTime

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    val list = listOf<String>("test", "list", "eagle", "test", "Car", "bus", "School", "sky")
    val listNums = listOf<Int>(5, 12, 435, 12, 456, 67, 3, 1, 10, 45, -45, 3, -1, 3 , 0 , 6)
    val listName1 = listOf<String>("Andrew", "Oleg", "Mark", "Sultan")
    val listName2 = listOf<String>("Grafield", "Oleg", "Mark", "Anthony")

    val people = mapOf(

        "Alice" to 25,

        "Bob" to 30,

        "Charlie" to 20,

        "David" to 25

    )

//    println(validateBrackets("( [ ]) { }"))

//    val bus = BusQueue()
//    bus.addPassenger("Andrew")
//    bus.addPassenger("Beric")
//    bus.addPassenger("Tom")
//    bus.addPassenger("Garry")
//    bus.addPassenger("Jim")
//    bus.addPassenger("Leo")
//    bus.addPassenger("Stan")
//    bus.boardBus()
//    println()
//    bus.boardBus()

}

// Task 1 Уникальные элементы (Set)
/*Условие:
Дана коллекция строк с повторяющимися элементами. Напиши функцию, которая возвращает только уникальные элементы.*/
fun getUniqueElements(list: List<String>) : Set<String> = list.toSet()

// Task 2 Подсчет количества слов (Map)
/*Условие:
Дана коллекция слов. Напиши функцию, которая возвращает Map, где ключ — это слово, а значение — количество его вхождений в коллекцию.*/
fun countingWords(list: List<String>) : Map<String, Int> = list.groupingBy { it }.eachCount()

// Task 3 Фильтрация списка (List)
/*Условие:
Дана коллекция чисел. Напиши функцию, которая возвращает только четные числа в том же порядке.*/
fun getEvenNumbers(list: List<Int>) : List<Int> = list.filter { it % 2 == 0 }

// Task 4 Объединение двух списков (List + Set)
/*Даны два списка имен. Некоторые имена могут повторяться в обоих списках. Напиши функцию, которая возвращает объединенный список без дубликатов.*/
fun unionWithoutDuplicates(list1: List<String>, list2: List<String>) : List<String> = (list1 + list2).toSet().toList()

// Task 5 Поиск самого частого элемента (List + Map)
/*Дан список чисел. Напиши функцию, которая возвращает число, встречающееся чаще всего. Если таких чисел несколько, верни любое из них.*/
fun getMostFrequentNumber(list: List<Int>): Int = list.groupingBy { it }.eachCount().maxBy { it.value }.key

// Task 6 Группировка объектов (List → Map)
/*Дан список людей (имя, возраст). Напиши функцию, которая группирует их по возрасту.*/
/*Пример:
data class Person(val name: String, val age: Int)

val people = listOf(
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 25),
    Person("David", 30),
    Person("Eve", 25)
)*/

fun groupByAge(list: List<Person>) : Map<Int, List<Person>> {
    return list.groupBy { it.age }
}

// Task 7 Разница между двумя списками (List → Set)
/*Даны два списка. Напиши функцию, которая возвращает элементы, которые есть в первом списке, но отсутствуют во втором.*/
/*Пример:
val list1 = listOf(1, 2, 3, 4, 5)
val list2 = listOf(4, 5, 6, 7, 8)*/

// Ожидаемый результат: [1, 2, 3]
fun getDifference(list1: List<Int>, list2: List<Int>) : List<Int> = list1 - list2

// Task 8 Объединение списков с условием (List + flatMap)
/*Дан список списков чисел. Напиши функцию, которая возвращает все числа, которые больше заданного значения n.
Пример:

val listOfLists = listOf(
    listOf(1, 2, 3),
    listOf(4, 5, 6),
    listOf(7, 8, 9)
)

val n = 5*/
// Ожидаемый результат: [6, 7, 8, 9]
fun filterNumbersGreaterThanN(list: List<List<Int>>, n: Int): List<Int> = list.flatMap { it -> it.filter { it > n }}

// Task 9 Поиск пересечений в списках (List + Set)
/*Даны три списка. Напиши функцию, которая возвращает элементы, которые присутствуют во всех трех списках.
Пример:
val list1 = listOf(1, 2, 3, 4, 5)
val list2 = listOf(4, 5, 6, 7, 8)
val list3 = listOf(5, 6, 7, 8, 9)*/

// Ожидаемый результат: [5]
fun findCommonElements(list1: List<Int>, list2: List<Int>, list3: List<Int>) : List<Int> = list1.toSet().intersect(list2).intersect(list3).toList()

// Task 10 Сортировка Map по значению (Map → List)
/*Дан Map, где ключ — имя, а значение — возраст. Напиши функцию, которая возвращает имена, отсортированные по возрасту (по возрастанию).

val people = mapOf(
    "Alice" to 25,
    "Bob" to 30,
    "Charlie" to 20,
    "David" to 25

)*/

// Ожидаемый результат: ["Charlie", "Alice", "David", "Bob"]
fun sortNamesByAge(map: Map<String, Int>) : List<String> = map.entries.sortedBy { it.value }.map { it.key }


// 🔹 Задачи на стеки
//Task 11 Проверка сбалансированных скобок
/*Дана строка, содержащая скобки (), [], {}. Проверить, правильно ли они расставлены.
Примеры:
"( [ ] ) { }" → true
"( [ ) ]" → false*/

fun validateBrackets(str: String) : Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = mutableListOf<Char>()

    for (char in str.replace(" ", "")) {
        when (char) {
            in pairs.values -> stack.add(char)
            in pairs.keys -> {
                if (stack.isEmpty() || stack.removeAt(stack.lastIndex) != pairs[char]) {
                    return false
                }
            }
            else -> continue
        }
    }
    return stack.isEmpty()
}

//Task 12 Переворот строки с помощью стека
/*Дана строка. Переверните её, используя стек.
Пример:

Вход: "kotlin"
Выход: "niltok"*/

fun reverseStringUsingStack(text: String): String {
    val stack = mutableListOf<Char>()
    val reversedText = StringBuilder()
    text.forEach { stack.add(it) }

    while (stack.isNotEmpty()) reversedText.append(stack.removeAt(stack.lastIndex))
    return reversedText.toString()
}

//Task 13 Проверка на палиндром с помощью очереди и стека
/*Дана строка. Проверить, является ли она палиндромом (читается одинаково слева направо и справа налево), используя стек и очередь.

пример:

Вход: "racecar"
Выход: true

Вход: "hello"
Выход: false*/

fun isPalindrome(s: String): Boolean {
    val stack = ArrayDeque<Char>() //LIFO
    val queue: Queue<Char> = LinkedList() //FIFO

    s.forEach {
        stack.add(it)
        queue.add(it)
    }

    while (stack.isNotEmpty() && queue.isNotEmpty()) {
        if (queue.poll() != stack.removeLast()) {
            return false
        }
    }
    return true
}

//Task 14 Обработка заказов в кафе
/*В кафе приходят заказы. Реализуйте систему обработки заказов в порядке их поступления.

addOrder(order: String) — добавить заказ в очередь.
processOrder() — обработать (вывести) следующий заказ.

нужно сделать свой класс CafeQueue у которого будут эти два метода и далее из main его вызывать

fun main() {
    val cafe = CafeQueue()
    cafe.addOrder("Кофе")
    cafe.addOrder("Чай")
    println(cafe.processOrder()) // Кофе
    println(cafe.processOrder()) // Чай
}*/

class CafeQueue {
    val queue: Queue<String> = LinkedList()

    fun addOrder(order: String) {
        queue.add(order)
    }

    fun processOrder(): String {
        return queue.poll()
    }
}

//Task 15 Симулятор автобусной остановки
/*На остановке стоит очередь пассажиров. Автобус забирает сразу 3 человека. Реализуйте:

addPassenger(name: String) — добавить пассажира.
boardBus() — забрать группу из 3 человек.*/

class BusQueue {
    val queue: Queue<String> = LinkedList()

    fun addPassenger(name: String) {
        queue.add(name)
    }

    fun boardBus() {
        if (queue.isNotEmpty() && queue.size >= 3) {
            for (passenger in 0..2) {
                println("${queue.poll()} got on the bus")
            }
        }
    }
}



// Задачи на first() и last()
// Task 16 Получить первый и последний элемент списка
/*Дан список чисел. Верните его первый и последний элементы в виде пары. Если список пуст, верните null.*/
fun getFirstAndLastElements(list: List<Int>) : Pair<Int, Int>? {
    if (list.isEmpty()) return null
    return Pair(list.first(), list.last())
}

// Task 17 Найти первый чётный и последний нечётный (используем find)
/*Дан список чисел. Найдите первый чётный и последний нечётный элементы.*/
fun findFirstEvenAndLastOdd(list: List<Int>) {
    val evenFirst = list.find { it % 2 == 0 }
    val evenLast = list.findLast { it % 2 == 0 }
    println(evenFirst)
    println(evenLast)
}



//Задачи на take() и drop()
// Task 18 Взять первые N элементов и перевернуть (take)
/*Дан список строк и число N. Верните первые N элементов в обратном порядке.*/
fun reverseFirstNElements(list: List<String>, n: Int): List<String> = list.take(n).reversed()

// Task 19 Пропустить первые K элементов (drop)
/*Дан список чисел и число K. Пропустите первые K элементов и верните оставшиеся.*/
fun skipFirstKElements(list: List<Int>, k: Int): List<Int> = list.drop(k)

// Task 20 Поиск последнего отрицательного числа (findLast)
/*Дан список чисел. Найдите последнее отрицательное число.*/
fun findLastNegativeNumber(list: List<Int>): Int? = list.findLast { it < 0 }



// Задачи на метод map()
// Task 21 Удвоение чисел в списке (map)
/*Дан список чисел. Создайте новый список, где каждое число умножено на 2*/
fun doubleNumbersInList(list: List<Int>): List<Int> = list.map { it * 2 }

// Task 22 Преобразование строк в их длины(map)
/*Дан список строк. Создайте список из длин этих строк.*/
fun convertStringsToLengths(list: List<String>): List<Int> = list.map { it.length }

// Task 23 Перевод температур из Цельсия в Фаренгейт (map)
/*Дан список температур в градусах Цельсия. Преобразуйте их в градусы Фаренгейта по формуле:
F = C * 9/5 + 32.*/
fun convertCelsiusToFahrenheit(listCelsius: List<Int>): List<Int> = listCelsius.map { it * 9/5 + 32 }