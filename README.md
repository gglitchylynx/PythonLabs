
<br> <br>
> # **Лабораторные работы и пояснения**

***

 ### <span style="color:#00a0fc"> 
 Репозиторий Романова Никиты(Семеновича) 408010 для лабораторных работ по Python
 </span>

 ***


 ## <span style="color:#00a0fc"> **lab7** </span>
Работа посвящена работе в API

Сделано:

>OpenWeatherMap.py - основная по требованию программа. В этой программе подключаемся к одноименному сайту по http и получаем значения для города, введенного в консоль
***
Пример работы:

`Введите название города (или 'exit' для выхода): Paris`

```cpp
ПОГОДА В ГОРОДЕ: Париж, FR
 Температура: 11.4°C
   Ощущается как: 11.0°C
   Минимальная: 10.2°C
   Максимальная: 12.3°C
 Влажность: 94%
 Давление: 989 гПа
 Погодные условия: Туман
 Скорость ветра: 5.14 м/с
   Направление ветра: 160° (Ю)
 Видимость: 5000 метров
 Облачность: 100%
 Восход: 10:07
 Закат: 20:02
```
***

>OpenNotifyOrg.py - второстепенная работа по вариантам. У меня последняя цифра в ису `0`, поэтому я и взял этот сайт. На этом сайте транслируются данные с МКС(кто на ней есть, где находится). В ходе выполнения программы появятся два файла: 
  `astronauts_in_space.json`
  `iss_position.json`
***
Пример работы:

`astronauts_in_space.json`

```json
{
  "people": [
    {
      "craft": "ISS",
      "name": "Oleg Kononenko"
    },
    {
      "craft": "ISS",
      "name": "Nikolai Chub"
    },
    {
      "craft": "ISS",
      "name": "Tracy Caldwell Dyson"
    },
    {
      "craft": "ISS",
      "name": "Matthew Dominick"
    },
    {
      "craft": "ISS",
      "name": "Michael Barratt"
    },
    {
      "craft": "ISS",
      "name": "Jeanette Epps"
    },
    {
      "craft": "ISS",
      "name": "Alexander Grebenkin"
    },
    {
      "craft": "ISS",
      "name": "Butch Wilmore"
    },
    {
      "craft": "ISS",
      "name": "Sunita Williams"
    },
    {
      "craft": "Tiangong",
      "name": "Li Guangsu"
    },
    {
      "craft": "Tiangong",
      "name": "Li Cong"
    },
    {
      "craft": "Tiangong",
      "name": "Ye Guangfu"
    }
  ],
  "number": 12,
  "message": "success",
  "retrieved_at": "2026-02-10T16:25:27.545742",
  "source": "open-notify.org/astros.json"
}
```
---
`iss_position.json`
```json
{
  "message": "success",
  "iss_position": {
    "latitude": "36.6351",
    "longitude": "8.3669"
  },
  "timestamp": 1770729928,
  "retrieved_at": "2026-02-10T16:25:29.349986",
  "readable_time": "2026-02-10 16:25:28 UTC",
  "source": "open-notify.org/iss-now.json"
}
```
***
>Miau.py - дополнительное задание, где генерируется изображения котика

Пример работы:

![ROS2 overdose](https://cs14.pikabu.ru/post_img/2022/05/21/11/1653160327265448506.jpg)


***

<br> <br>

 ## <span style="color:#00a0fc"> **lab8** </span>

 Работа посвящена взаимодействием с OpenCV

 ***

 Сделано:

 >filtering.py - программа редактирования изображения, соответствующее варианту(инверсия цвета и переворот)

 Пример работы:

 ![ROS2 overdose](lab8/variant_10_threshold.jpg)

 ***

 >FlyInTheHole.py (игра слов от фразы "Fire in the hole!") - тут совмещены остальные пункты работы. Камера подключается, запускается окно и программа таргетит черный цвет(в условиях лабораторной - черную точку на листе). После обнаружения этой точки на нее накладывается муха и при пересечении центра картинка инвертируется(как и все остальное)

 Пример работы:

  ![site](lab8/фрик.gif)


***

<br> <br>

 ## <span style="color:#00a0fc"> **lab9** </span> 

 Работа посвящена работе с Flask

 Сделано:

 >Сайт соответствует варианту 10. Работа с базой данных, дизайн через css, подключение к базе данных с помощью python и функционал с помощью javascript - все реализовано успешно 
    >>Дизайн отличный (ну а как иначе), так как я занимался html и в моем репозитории можете посмотреть [мой сайт](https://github.com/gglitchylynx/ml_site "mlsite") (только если скачать и локально запустить. Подключение к базе данных отсутствует)

 Пример работы:

 ![site](lab9/lab9.png)


***

<br> <br>

 ## <span style="color:#00a0fc"> **lab10** </span> 


***

<br> <br>

 ## <span style="color:#00a0fc"> **project** </span> 


***