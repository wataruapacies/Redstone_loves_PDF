import os
import glob
import PyPDF2

def split():
    split_dir = "split"
    if not os.path.exists(split_dir):
        os.mkdir(split_dir)
    pdf_list = glob.glob("*.pdf")
    print("どのPDFを分割するん？")
    print("番号で入力して")
    for i in range(len(pdf_list)):
        print(i+1,pdf_list[i])
    number = int(input())
    pdf = pdf_list[number-1]
    print(pdf,"を分割します")
    reader = PyPDF2.PdfReader(pdf)
    print(len(reader.pages),"ページありますが，何ページ目で分割しますか？")
    print("※複数の数字の入力可能")
    print("（例）20 25 60")
    print("順番は問わない")
    number_list = list(map(int,input().split()))
    number_list.sort()
    
    #print(number_list)
    number_list.append(len(reader.pages))
    for i in range(len(number_list)):
        pdf_pages = PyPDF2.PdfWriter()
        if i == 0:
            start_page = 0
        else:
            start_page = number_list[i-1]
        end_page = number_list[i]
        #print('i',i)
        for j in range(start_page,end_page):
            #print("j",j)
            p = reader.pages[j]
            pdf_pages.add_page(p)
        fnum = "{0:03d}".format(i+1)
        with open(os.path.join(split_dir,f"{pdf}_{fnum}.pdf"),mode="wb") as f:
            pdf_pages.write(f)
    print("完了")
        
        
    

if __name__ == "__main__":
    split()