import os
import argparse
import pytesseract
import matplotlib.pyplot as plt
import tensorflow as tf
from doctr.utils.visualization import visualize_page
import cv2
from documents import DocumentFile
from doctr.models import ocr_predictor
from paddleocr import PaddleOCR


tf.get_logger().setLevel('ERROR')
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
if any(gpu_devices):
    tf.config.experimental.set_memory_growth(gpu_devices[0], True)


def main():

    parser = argparse.ArgumentParser(
        description="Runs on files inside a directory")
    parser.add_argument(
        "--dir",
        help="Absolute path to directory",
        required=True)
    parser.add_argument(
        "--ocr",
        choices=[
            'tesseract',
            'paddle',
            'doctr'],
        help="library to use",
        required=True)
    args = parser.parse_args()

    filenames = os.listdir(args.dir)
    #tesseract
    if args.ocr == "tesseract":
        for f in filenames:
            # tesseract
            if f.endswith(('.pdf', '.png', '.jpeg', '.jpg')):
                file_to_read = args.dir + "/" + f
                result_file = open(
                    args.dir + "/" + f.split(".")[0] + ".txt", "w+")
                if f.endswith('.pdf'):
                    doc = DocumentFile.from_pdf(file_to_read).as_images(
                        output_size=(1024, 1024))

                else:
                    doc = DocumentFile.from_images(file_to_read)
                result = str(pytesseract.image_to_string(doc[0])).strip()
                result_file.write(result)

                result_file.close()

    # doctr
    elif args.ocr == "doctr":
        model = ocr_predictor(
            det_arch='db_resnet50',
            reco_arch='crnn_vgg16_bn',
            pretrained=True)
        for f in filenames:
            if f.endswith(('.pdf', '.png', '.jpeg', '.jpg')):
                file_to_read = args.dir + "/" + f
                if f.endswith('.pdf'):
                    doc = DocumentFile.from_pdf(file_to_read).as_images(
                        output_size=(1024, 1024))
                else:
                    doc = DocumentFile.from_images(file_to_read)

                result_file = open(
                    args.dir + "/" + f.split(".")[0] + ".txt", "w+")

                
                out = model(doc, training=False)

                result = out.export()

                for b in result['pages'][0]['blocks']:
                    for l in b['lines']:
                        for w in l['words']:
                            result_file.write(
                                w["value"] + "  " + str(w["geometry"]) + "\n")

                result_file.close()

    #paddle
    elif args.ocr == "paddle":
        ocr = PaddleOCR(lang='en')
        for f in filenames:

            if f.endswith(('.pdf', '.png', '.jpeg', '.jpg')):
                file_to_read = args.dir + "/" + f
                if f.endswith('.pdf'):
                    doc = DocumentFile.from_pdf(file_to_read).as_images(
                        output_size=(1024, 1024))
                else:
                    doc = DocumentFile.from_images(file_to_read)

                result_file = open(
                    args.dir + "/" + f.split(".")[0] + ".txt", "w+")

                result = ocr.ocr(doc[0])

                result_file.write(str(result))
                result_file.close()


if __name__ == '__main__':
    main()
