Catsay - программа, которая генерирует изображения кота в формате ASCII с вашим сообщением

Для установки catsay потребуется <b>poetry</b>:

`pip install --user poetry`

Затем в директории проекта введите:

`make build install`

Для запуска достаточно ввести в консоль:

`cat-say`

Программа запросит ввести сообщение:

```
What cat should say?
 --- {Ваше сообщение} 
```

Затем выведет:

```
  -----------------------------------------
 /                                         \
|             {Ваше сообщение}              |
 \                                         /
  -----------------------------------------
 \
  \    |\     /|
   \   |_\___/_| 
    \  | o   o |              _____
     --(   *   )--           /     | 
        \_____/\____________/    \/ 
          \                |
           |   |___________|
           |   |         | |
          /   /          / /
```
