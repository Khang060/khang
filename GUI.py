from tkinter import *
import tkinter
from threading import Thread
from tkinter.ttk import Combobox
from  tkinter import messagebox
from docutils.nodes import comment
from joblib import dump, load
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
# #Load model bằng joblib
# navie = load('D:/DESKTOP/hoc tap/year 3 - hk2/May hoc/model_NavieBayes.joblib')


def Model(arr):
    # Tạo mô hình ANN 3 lớp
    modelAnn = Sequential()
    # Tạo lớp ẩn đầu tiên là lớp input đầu vào
    modelAnn.add(Dense(units = 128, activation='relu', kernel_initializer = 'he_uniform', input_dim = 13))
    # Tạo thêm lớp ẩn thứ 2
    modelAnn.add(Dense(units = 16, activation='relu', kernel_initializer = 'he_uniform'))
    # Mạng Ann với 2 lớp trên tạo ra lớp đầu ra output cho lớp này
    modelAnn.add(Dense(units = 1, activation = 'sigmoid', kernel_initializer = 'glorot_uniform'))
    modelAnn.load_weights("D:/DESKTOP/hoc tap/year 3 - hk2/May hoc/ModelAnn.h5")
    dudoan = modelAnn.predict([Arr])
    return dudoan


# dudoan = navie.predict([[56, 1, 1, 120, 236, 0, 1, 178, 0, 0.8, 2, 0, 2]])



Arr = [56, 1, 1, 120, 236, 0, 1, 178, 0, 0.8, 2, 0, 2]
# Arr = []
win = Tk()
win.title('Ứng dụng dự đoán bệnh tim')
# kich thước from
win.geometry('670x400')

# thêm label
lbl = Label(win, text = 'Chuẩn', fg= 'red', font=('Arial', 30),)
lbl.grid(column=0, row=1)
lbl_ = Label(win, text = 'Đoán', fg= 'red', font=('Arial', 30),)
lbl_.grid(column=0, row=2)
lbl_ = Label(win, text = 'Bệnh', fg= 'red', font=('Arial', 30),)
lbl_.grid(column=0, row=3)
lbl_ = Label(win, text = 'Tim', fg= 'red', font=('Arial', 30),)
lbl_.grid(column=0, row=4)
lbl_ = Label(win, text = 'Mạch', fg= 'red', font=('Arial', 30),)
lbl_.grid(column=0, row=5)

lbl0 = Label(win, text = 'Kết quả: ', fg= 'blue', font=('Arial', 15))
lbl0.grid(column=2, row=9)

lbl1 = Label(win, text = 'Age', font=('Arial', 15))
lbl1.grid(column=1, row=1)
lbl2 = Label(win, text = 'Sex', font=('Arial', 15))
lbl2.grid(column=1, row=2)
lbl3 = Label(win, text = 'cp', font=('Arial', 15))
lbl3.grid(column=1, row=3)
lbl4 = Label(win, text = 'trestbps', font=('Arial', 15))
lbl4.grid(column=1, row=4)
lbl5 = Label(win, text = 'Cholestoral', font=('Arial', 15))
lbl5.grid(column=1, row=5)
lbl6 = Label(win, text = 'fbs', font=('Arial', 15))
lbl6.grid(column=1, row=6)
lbl7 = Label(win, text = 'restecg', font=('Arial', 15))
lbl7.grid(column=3, row=1)
lbl8 = Label(win, text = 'thalach', font=('Arial', 15))
lbl8.grid(column=3, row=2)
lbl9 = Label(win, text = 'exang', font=('Arial', 15))
lbl9.grid(column=3, row=3)
lbl10 = Label(win, text = 'oldpeak', font=('Arial', 15))
lbl10.grid(column=3, row=4)
lbl11 = Label(win, text = 'slope', font=('Arial', 15))
lbl11.grid(column=3, row=5)
lbl12 = Label(win, text = 'ca', font=('Arial', 15))
lbl12.grid(column=3, row=6)
lbl13 = Label(win, text = 'thal', font=('Arial', 15))
lbl13.grid(column=1, row=7)

# them checkbox

# them combobox
com1 = Combobox(win)
com1['values'] = ("Nam", "Nữ")
com1.grid(column=2,row=2)
com2 = Combobox(win)
com2['values'] = ("Cơn đau thắt ngực điển hình", "Đau thắt ngực không điển hình", "Không đau thắt ngực", "Không có triệu chứng")
com2.grid(column=2,row=3)
com3 = Combobox(win)
com3['values'] = ("True", "False")
com3.grid(column=2,row=6)
com4 = Combobox(win)
com4['values'] = ("Bình thường", "Có bất thường sóng ST-T (đảo ngược sóng T và / hoặc ST chênh lên hoặc xuống> 0,05 mV)", "Hiển thị phì đại thất trái có thể xảy ra hoặc xác định theo tiêu chuẩn của Estes")
com4.grid(column=4,row=1)
com5 = Combobox(win)
com5['values'] = ("Có", "Không")
com5.grid(column=4,row=3)
com6 = Combobox(win)
com6['values'] = ("Uploping", "Bằng phẳng", "Downloping")
com6.grid(column=4,row=5)
com7 = Combobox(win)
com7['values'] = ("0", "1", "2", "3")
com7.grid(column=4,row=6)
com8 = Combobox(win)
com8['values'] = ("Bình thường", "Khuyết tật cố định", "Khiếm khuyết có thể đảo ngược")
com8.grid(column=2,row=7)

#xet thuộc tính chọn 1 dòng
com1.current(0)
com2.current(0)
com3.current(0)
com4.current(0)
com5.current(0)
com6.current(0)
com7.current(0)
com8.current(0)




# thêm textbox
txt1 = IntVar()
txt2 = IntVar()
txt3 = IntVar()
txt4 = IntVar()
txt5 = IntVar()
#Age
txt1 = Entry(win, width= 23, textvariable = txt1)
txt1.grid(column=2, row=1)
#
txt2 = Entry(win, width= 23, textvariable = txt2)
txt2.grid(column=2, row=4)
txt3 = Entry(win, width= 23, textvariable = txt3)
txt3.grid(column=2, row=5)
txt4 = Entry(win, width= 23, textvariable = txt4)
txt4.grid(column=4, row=2)
txt5 = Entry(win, width= 23, textvariable = txt5)
txt5.grid(column=4, row=4)

# Hàm
def Nhaptt():
    #Age
    Arr[0] = (int(txt1.get())-29)/(77-29)
    #Sex
    if com1.get() == 'Nam':
        Arr[1] = 1

    if com1.get() == 'Nữ':
        Arr[1] = 0

    #cp: đau ngực kiểu
    if com2.get() == 'Cơn đau thắt ngực điển hình':
        Arr[2] = 1
    if com2.get() == 'Đau thắt ngực không điển hình':
        Arr[2] = 2
    if com2.get() == 'Không đau thắt ngực':
        Arr[2] = 3
    if com2.get() == 'Không có triệu chứng':
        Arr[2] = 4
    #trestbps: huyết áp lúc nghỉ (tính bằng mm Hg khi nhập viện)
    Arr[3] = (int(txt2.get())-94)/(200-94)
    #chol: cholestoral trong huyết thanh tính bằng mg / dl
    Arr[4] = (int(txt3.get())-126)/(564-126)
    #fbs: (đường huyết lúc đói> 120 mg / dl)
    if com3.get() == 'True':
        Arr[5] = 1
    if com3.get() == 'False':
        Arr[5] = 0
    #restecg: kết quả điện tâm đồ lúc nghỉ
    if com4.get() == 'Bình thường':
        Arr[6] = 0
    if com4.get() == 'Có bất thường sóng ST-T (đảo ngược sóng T và / hoặc ST chênh lên hoặc xuống> 0,05 mV)':
        Arr[6] = 1
    if com4.get() == 'Hiển thị phì đại thất trái có thể xảy ra hoặc xác định theo tiêu chuẩn của Estes':
        Arr[6] = 2
    #thalach: nhịp tim tối đa đạt được
    Arr[7] = (int(txt4.get())-71)/(202-71)
    #exang: đau thắt ngực do tập thể dục (1 = có; 0 = không)
    if com5.get() == 'Có':
        Arr[8] = 1
    if com5.get() == 'Không':
        Arr[8] = 0
    #oldpeak = ST trầm cảm gây ra do tập thể dục liên quan đến nghỉ ngơi
    Arr[9] = (int(txt5.get())-0)/(6.2-0)
    #slope: độ dốc của đoạn ST tập luyện đỉnh
    if com6.get() == 'Uploping':
        Arr[10] = 1
    if com6.get() == 'Bằng phẳng':
        Arr[10] = 2
    if com6.get() == 'Downloping':
        Arr[10] = 3
    #ca: số lượng các mạch chính (0-3) được tô màu bởi bột màu
    Arr[11] = int(com7.get())
    #thal:
    if com8.get() == 'Bình thường':
        Arr[12] = 1
    if com8.get() == 'Khuyết tật cố định':
        Arr[12] = 2
    if com8.get() == 'Khiếm khuyết có thể đảo ngược':
        Arr[12] = 3
    print(Arr)

def Dudoan():
    # dudoan = navie.predict([Arr])
    thread = Thread(target=Nhaptt())
    thread.start()
    dudoan = Model(Arr)
    a = len(Arr)
    if Arr[0] < 0 or Arr[0] > 1:
        messagebox.showinfo("Thông báo","Vui lòng nhập tuổi chính xác")
        return
    if Arr[3] < 0 or Arr[3] > 1:
        messagebox.showinfo("Thông báo","Vui lòng nhập đúng huyết áp")
        return
    if Arr[4] < 0 or Arr[4] > 1:
        messagebox.showinfo("Thông báo","Vui lòng nhập đúng cholestoral trong huyết thanh")
        return
    if Arr[7] < 0 or Arr[7] > 1:
        messagebox.showinfo("Thông báo","Vui lòng nhập đúng nhịp tim tối đa đạt được")
        return
    if Arr[9] < 0 or Arr[9] > 1:
        messagebox.showinfo("Thông báo","Vui lòng nhập đúng oldpeak")
        return
    if a == 13:
        # Du doan của Navie Bayes
        # if dudoan == 0:
        #     kq = 'Không có bệnh'
        #     lbl0.configure(text = 'Dự đoán: ' + kq)
        #     return
        # if dudoan == 1:
        #     kq = 'Có bệnh'
        #     lbl0.configure(text = 'Dự đoán: ' + kq)
        #     return
        # Du đoán của Ann
        if dudoan > 0.5:
            kq = 'Có bệnh'
            lbl0.configure(text = 'Dự đoán: ' + kq)
            return
        else:
            kq = 'Không có bệnh'
            lbl0.configure(text='Dự đoán: ' + kq)
            return

# thêm button
btn1 = Button(win, text = 'Dự đoán', font=('Arial', 10), command= Dudoan)
btn1.grid(column=2,row=8)

# Hàm



win.mainloop()