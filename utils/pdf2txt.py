import os, codecs
import multiprocessing
import pdfplumber

pdf_path = "..\\data\\neeq_annual_report_2018H1"
txt_path = "..\\data\\neeq_annual_report_2018H1_txt"


def convert(start, end):
    cnt = 0
    for root, dirs, files in os.walk(pdf_path):
        for f in files[start:end]:
            cnt = cnt + 1
            print("{}/({}-{})".format(cnt, start, end))
            if f.endswith("pdf"):
                try:
                    with pdfplumber.open(os.path.join(pdf_path, f)) as pdf:
                        txt_filename = f.split(".")[-2] + ".txt"
                        with codecs.open(os.path.join(txt_path, txt_filename), "w", encoding="utf-8") as new_f:
                            for page in pdf.pages:
                                new_f.write(page.extract_text())
                except:
                    print("one failed")


if __name__ == "__main__":
    total = 10472 - 1100
    for i in range(4):
        t = multiprocessing.Process(target=convert, args=(int(1100+(10472-1100)/4*i),int((10472-1100)/4*(i+1)+1100)))
        t.start()