# allin1_ocr
Choose from paddleocr, teseract or doctr to perfrom OCR.

Installation:</br>

git clone https://<i></i>github.com/maylad31/allin1_ocr.git </br>

cd allin1_ocr</br>

pip install -r requirements.txt

For using tesseract, you need to install tesseract:

sudo apt install tesseract-ocr</br>
sudo apt install libtesseract-dev</br>

**Tested with python3.8.6 on linux


Run:</br>
python app.py --dir /home/mayank/test --ocr paddle </br>   (choose from 'tesseract', 'paddle', 'doctr') </br>

Perfroms ocr on all the files in the directory and saves the results to corresponding text files. You can run on pdf, png, jepg, jpg.







