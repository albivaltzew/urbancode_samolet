# urbancode_samolet
Хакатон URBANCODE от компании Самолет

## Часть 1 - Детекция ячеек в многоэтажном доме.
1. Для перевода аннотаций в YOLO формат использовался репозиторий coco2yolo (https://github.com/tw-yshuang/coco2yolo.git)
2. Почистили датасет от фотографий где есть обшивка\утеплитель
3. Разметка данных CVAT 149 изображения (6k class objects)
4. Аугментация данных albumentations. (https://github.com/EslamAsfour/Augmentation-using-Albumentations)
5. Remapping dataset - Datumaro. Смена классов
6. Проверка Dataset в roboflow
7. Запуск обучения YOLOv8n и YOLOv8m на 100 эпох.
8. TTA YOLO score +5%
9. Auto-rectification - избавление от искажения перспективы и дисторсии

## Часть 2 - Координаты ячеек 
1. Разработка алгоритма
   Были испробованы методы:
   1. Сортировка
   2. Квантование координат
   3. KMeans
   4. Агломеративная кластеризация
   5. DBSCAN
   6. Графы
2. Причесывание датасета
   1. Удаление изображений с несколькими домами
   2. Поиск новых изображений для валидационной выборки
3. Тренировка YOLOv8n на новом дс
4. Препроцессинг перед тренировкой - defisheye

   
   



Сcылки:

Fish Eye Rectification:

Auto-rectification имплементирована в последнем решении:
https://github.com/chsasank/Image-Rectification

Ревью по избавлению от Дисторсии:

https://github.com/bchao1/awesome-image-rectification

DL methods: 

https://github.com/xiaoyu258/GeoProj - не работает (не обучена??)
https://github.com/ByronHsu/FEGAN
https://github.com/uof1745-cmd/PCN
https://github.com/alexvbogdan/DeepCalib

Аlbumentations:

https://github.com/EslamAsfour/Augmentation-using-Albumentations/blob/main/README.md

Datumaro:

https://openvinotoolkit.github.io/datumaro/latest/docs/get-started/quick-start-guide/examples.html

Аlbumentations погода:

https://colab.research.google.com/github/albumentations-team/albumentations_examples/blob/colab/example_weather_transforms.ipynb#scrollTo=3J6MeU2T5kwP&uniqifier=1

Используемые метрики Pascal VOC

https://github.com/rafaelpadilla/Object-Detection-Metrics
