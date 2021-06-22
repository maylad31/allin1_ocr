# allin1_ocr
Choose from paddleocr, python-doctr or tesseract to perfrom OCR.

**Installation:**</br>

git clone https://<i></i>github.com/maylad31/allin1_ocr.git </br>

cd allin1_ocr</br>

pip install -r requirements.txt

For using tesseract, you need to install tesseract:

sudo apt install tesseract-ocr</br>
sudo apt install libtesseract-dev</br>

Tested with python3.8 on linux


**How to run:**</br>
python app.py --dir /home/mayank/test --ocr paddle </br>   (choose from 'paddle', 'doctr','tesseract') </br>

Perfroms ocr on all the files in the directory and saves the results to corresponding text files. You can run on pdf, png, jpeg, jpg.

If you ask me, paddleocr is fast and reasonable accurate. Doctr is good too.

You are welcome to add any other library.</br>

Always looking for opoortunities to enhance my skills, contact me at mynameladdha@gmail.com







