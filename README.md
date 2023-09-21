# urbancode_samolet
Хакатон URBANCODE от компании Самолет

1. Для перевода аннотаций в YOLO формат использовался репозиторий coco2yolo (https://github.com/tw-yshuang/coco2yolo.git)
2. Почистили датасет от фотографий где есть обшивка\утеплитель
3. Разметка данных CVAT 149 изображения (6k class objects)
4. Аугментация данных albumentations. (https://github.com/EslamAsfour/Augmentation-using-Albumentations)
5. Remapping dataset - Datumaro. Смена классов.
6. Проверка Dataset в roboflow.
7. Запуск обучения YOLOv8n и YOLOv8m на 100 эпох.
   


Заметки:
сети для Fish Eye Rectification

https://github.com/ByronHsu/FEGAN
https://github.com/uof1745-cmd/PCN
https://github.com/alexvbogdan/DeepCalib

repo for albumentations
https://github.com/EslamAsfour/Augmentation-using-Albumentations/blob/main/README.md


Datumaro:
https://openvinotoolkit.github.io/datumaro/latest/docs/get-started/quick-start-guide/examples.html

albumentations weather
https://colab.research.google.com/github/albumentations-team/albumentations_examples/blob/colab/example_weather_transforms.ipynb#scrollTo=3J6MeU2T5kwP&uniqifier=1
