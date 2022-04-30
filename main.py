import argparse
import os

import piexif
from PIL import Image, ImageOps


def convert_exif(Image, exif_0, exif_1, exif):
    # 4.6.4 TIFF Rev. 6.0 Attribute Information
    # Image width ImageWidth 256 100 SHORT or LONG 1
    # Image height ImageLength 257 101 SHORT or LONG
    # Orientation of image Orientation 274 112 SHORT 1
    # Image resolution in width direction XResolution 282 11A RATIONAL 1
    # Image resolution in height direction YResolution 283 11B RATIONAL 1

    # 4.6.5 Exif IFD Attribute Information
    # SubjectArea 37396 ; [X, Y] / [X, Y, R] / [X, Y, W, H]

    # Valid image width PixelXDimension 40962 A002
    # Valid image height PixelYDimension 40963 A003

    # Focal plane X resolution FocalPlaneXResolution 41486 A20E
    # Focal plane Y resolution FocalPlaneYResolution 41487 A20F
    # Subject location SubjectLocation 41492 A214 ; [X, Y]

    if 0x112 in exif_0 and exif_0[0x112] in [5, 6, 7, 8]:
        # try:
        #     exif[0x100], exif[0x101] = exif[0x101], exif[0x100]
        # except:
        #     exif[0x100], exif[0x101] = Image.width, Image.height

        try:
            exif_1[0x11A], exif_1[0x11B] = exif_1[0x11B], exif_1[0x11A]
            exif_0[0x11A], exif_0[0x11B] = exif_0[0x11B], exif_0[0x11A]
        except:
            pass

        try:
            tmp = list(exif[37396])
            tmp[0], tmp[1] = tmp[1], tmp[0]
            if len(tmp) == 4:
                tmp[2], tmp[3] = tmp[3], tmp[2]
            exif[37396] = type(exif[37396])(tmp)
        except:
            pass

        try:
            exif[0xA002], exif[0xA003] = exif[0xA003], exif[0xA002]
        except:
            exif[0xA002], exif[0xA003] = Image.height, Image.width

        try:
            exif[0xA20E], exif[0xA20F] = exif[0xA20F], exif[0xA20E]
        except:
            pass

        try:
            exif[0xA214] = exif[0xA214][::-1]
        except:
            pass
    exif_0[0x112] = 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="image reorientation")
    parser.add_argument("-i", "-s", "--input", type=str, nargs="*", help="source files")
    parser.add_argument("-o", "-d", "--output", type=str, help="destination directory")
    args = parser.parse_args()

    for F in args.input:
        image = Image.open(F)
        exif_data = piexif.load(image.info["exif"])
        image = ImageOps.exif_transpose(image)
        convert_exif(image, exif_data["0th"], exif_data["1st"], exif_data["Exif"])

        image.save(
            os.path.join(args.output, os.path.basename(F)),
            exif=piexif.dump(exif_data),
        )
