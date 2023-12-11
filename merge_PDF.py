import os
import glob
import PyPDF2

def merge():
    merge_dir = "merge"
    if not os.path.exists(merge_dir):
        os.mkdir(merge_dir)
    os.chdir(merge_dir)
    pdf_list = glob.glob("*.pdf")
    #print(pdf_list)
    if len(pdf_list) == 0:
        print("結合したい.pdfファイルをmergeディレクトリに入れなさいよ")
        exit()
    merger = PyPDF2.PdfMerger()
    for i in range(len(pdf_list)):
        merger.append(pdf_list[i])
    os.chdir("..")
    merger.write('merged.pdf')
    merger.close()
    



if __name__ == "__main__":
    merge()