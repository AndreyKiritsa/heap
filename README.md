# heap
Проверка на корректность "неубывающая пирамида"

Структуру данных «куча», или, более конкретно, «неубывающая пирамида», можно реализовать на основе массива.

Для этого должно выполнятся основное свойство неубывающей пирамиды, которое заключается в том, что для каждого *1 <= i <= n* выполняются условия:

1. если 2*i <= n* , то *a|i| <= a|2i|
2. если 2*i+1 <= n*, то *a|i| <= a|2i+1|

Дан массив целых чисел. Определите, является ли он неубывающей пирамидой.

## Формат входного файла
Первая строка входного файла содержит целое число *n(1 <= n <= 10^6)*. Вторая строка содержит *n* целых чисел, по модулю не превосходящих *2* в степени *10^6*.

## Формат выходного файла
Выведите «YES», если массив является неубывающей пирамидой, и «NO» в противном случае.

## Пример
|input.txt|output.txt|
|---------|----------|
|5  |NO|
|1 0 1 2 0 ||
|5|YES|
|1 3 2 5 4||
