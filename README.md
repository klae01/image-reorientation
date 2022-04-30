reorient image and change EXIF data


## usage

```shell
usage: main.py [-h] [-i [INPUT ...]] [-o OUTPUT]

image reorientation

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT ...], -s [INPUT ...], --input [INPUT ...]
                        source files
  -o OUTPUT, -d OUTPUT, --output OUTPUT
                        destination directory
```


## example
``` shell
>> python3 main.py -i IMG_8741.jpg -o converted/
>> exif IMG_8741.jpg
EXIF tags in 'IMG_8741.jpg' ('Motorola' byte order):
--------------------+----------------------------------------------------------
Tag                 |Value
--------------------+----------------------------------------------------------
Manufacturer        |Apple
Model               |iPhone 12 Pro
Orientation         |Right-top
X-Resolution        |72
Y-Resolution        |72
Resolution Unit     |Inch
Software            |15.4.1
Date and Time       |2022:04:20 18:00:45
YCbCr Positioning   |Centered
...
Focal Length        |4.2 mm
Subject Area        |Within rectangle (width 2213, height 1327) around (x,y) = 
Maker Note          |1430 bytes undefined data
Sub-second Time (Ori|191
Sub-second Time (Dig|191
FlashPixVersion     |FlashPix Version 1.0
Color Space         |Uncalibrated
Pixel X Dimension   |4032
Pixel Y Dimension   |3024
Sensing Method      |One-chip color area sensor
Scene Type          |Directly photographed
Exposure Mode       |Auto exposure
White Balance       |Auto white balance
Focal Length in 35mm|26
Scene Capture Type  |Standard
Lens Specification  |1.540000,  6, 1.6, 2.4
...
GPS Date            |2022:04:20
GPS Horizontal Posit|1414
--------------------+----------------------------------------------------------
EXIF data contains a thumbnail (10525 bytes).
>> exif converted/IMG_8741.jpg
EXIF tags in 'converted/IMG_8741.jpg' ('Motorola' byte order):
--------------------+----------------------------------------------------------
Tag                 |Value
--------------------+----------------------------------------------------------
Manufacturer        |Apple
Model               |iPhone 12 Pro
Orientation         |Top-left
X-Resolution        |72
Y-Resolution        |72
Resolution Unit     |Inch
Software            |15.4.1
Date and Time       |2022:04:20 18:00:45
YCbCr Positioning   |Centered
...
Focal Length        |4.2 mm
Subject Area        |Within rectangle (width 1327, height 2213) around (x,y) = 
Maker Note          |1430 bytes undefined data
Sub-second Time (Ori|191
Sub-second Time (Dig|191
FlashPixVersion     |FlashPix Version 1.0
Color Space         |Uncalibrated
Pixel X Dimension   |3024
Pixel Y Dimension   |4032
Sensing Method      |One-chip color area sensor
Scene Type          |Directly photographed
Exposure Mode       |Auto exposure
White Balance       |Auto white balance
Focal Length in 35mm|26
Scene Capture Type  |Standard
...
GPS Date            |2022:04:20
GPS Horizontal Posit|1414
--------------------+----------------------------------------------------------
EXIF data contains a thumbnail (10525 bytes).

```
