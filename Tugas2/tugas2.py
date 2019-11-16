import random
import os
import pandas 
import numpy

data_latih = pandas.read_csv('D:\Dokumen dan Tugas Kuliah\Tugas Kuliah\Kecerdasan Buatan\Tugas2\data_latih.csv')
data_test  = pandas.read_csv('D:\Dokumen dan Tugas Kuliah\Tugas Kuliah\Kecerdasan Buatan\Tugas2\data_test.txt')




gen_size = 15


list_data_latih = data_latih.values.tolist()
new_data_latih = []
for data_train in list_data_latih:
    temp =[]
    for index in range(0, len(data_train)):
        if index == 0:
            if "Rendah" in data_train[index]:
                temp.append('100')
            elif "Normal" in data_train[index]:
                temp.append('010')
            elif "Tinggi" in data_train[index]:
                    temp.append('001')
        elif index == 1 :
            if "Pagi" in data_train[index]:
                temp.append('1000')
            elif "Siang" in data_train[index]:
                temp.append('0100')
            elif "Sore" in data_train[index]:
                temp.append('0010')
            elif "Malam" in data_train[index]:
                temp.append('0001')
        elif index == 2 :
            if "Hujan" in data_train[index]:
                temp.append('1000')
            elif "Rintik" in data_train[index]:
                temp.append('0100')
            elif "Berawan" in data_train[index]:
                temp.append('0010')
            elif "Cerah" in data_train[index]:
                temp.append('0001')
        elif index == 3 :
            if "Rendah" in data_train[index]:
                temp.append('100')
            elif "Normal" in data_train[index]:
                temp.append('010')
            elif "Tinggi" in data_train[index]:
                temp.append('001')
        elif index == 4 :
            if "Ya" in data_train[index]:
                temp.append('1')
            elif "Tidak" in data_train[index]:
                temp.append('0')
    new_data_latih.append(temp)
nilai_data_latih = []
for idx in new_data_latih:
    nilai_data_latih.append("".join(idx))
#print(nilai_data_latih) 

list_data_test = data_test.values.tolist()
new_data_test = []
for data in list_data_test:
    temp =[]
    for index in range(0, len(data)):
        if index == 0:
            if "Rendah" in data[index]:
                temp.append('100')
            elif "Normal" in data[index]:
                temp.append('010')
            elif "Tinggi" in data[index]:
                    temp.append('001')
        elif index == 1 :
            if "Pagi" in data[index]:
                temp.append('1000')
            elif "Siang" in data[index]:
                temp.append('0100')
            elif "Sore" in data[index]:
                temp.append('0010')
            elif "Malam" in data[index]:
                temp.append('0001')
        elif index == 2 :
            if "Hujan" in data[index]:
                temp.append('1000')
            elif "Rintik" in data[index]:
                temp.append('0100')
            elif "Berawan" in data[index]:
                temp.append('0010')
            elif "Cerah" in data[index]:
                temp.append('0001')
        elif index == 3 :
            if "Rendah" in data[index]:
                temp.append('100')
            elif "Normal" in data[index]:
                temp.append('010')
            elif "Tinggi" in data[index]:
                temp.append('001')
       
    new_data_test.append(temp)
nilai_data_test = []
for idx in new_data_test:
    nilai_data_test.append("".join(idx))
#print(nilai_data_test) 

class models(object):
    kromosom = []
    aturan = []
    prediksi = []
    fitness = None
    def __init__(self, gen):
        self.kromosom = gen
        self.inisialisasi()

    def inisialisasi(self):
        aturan = []
        for i  in range(0, int(len(self.kromosom)/gen_size)):
            temp = []
            for j in range(i*15, 15*(i+1)):
                temp.append(self.kromosom[j])
            aturan.append(temp)
        self.aturan = aturan

#modelss = models(list("101010101010101101010101010101101010101010101"))
#print(modelss.aturan)
    def prediksi_list(self, data_string):
        list_prediksi = []
        for aturan in self.aturan :
            temp = []
            for data in data_string :
                tmp = []
                for index_dt in range(0,len(data)-1) :
                    if data[index_dt] == '1' :
                        if aturan[index_dt] == '1':
                            tmp.append(True)
                        else:
                            tmp.append(False)
                if False in tmp:
                    if aturan[-1] == '1':
                        temp.append(False)
                    else :
                        temp.append(True)
                else:
                    if aturan[-1] == '1' :
                        temp.append(True)
                    else:
                        temp.append(False)

            
            list_prediksi.append(temp)
        prediksi_aturan = []
        for y in range(0, len(list_prediksi[0])) :
            temp_list = []
            for x in range(0, len(list_prediksi)) :
                #print(type(list_prediksi[x][y]))
                temp_list.append(list_prediksi[x][y])
            #print(temp_list)
            prediksi_aturan.append(temp_list)
        list_fin = []
        for prediksi in prediksi_aturan:
            if True in prediksi :
                list_fin.append(True)
            else:
                list_fin.append(False)
        return list_fin
#modelss = models(list("111111111111111000111111111111"))
#print((modelss.prediksi_list(nilai_data_latih)))
#print((modelss.prediksi_list(nilai_data_test)))

    def hitung_fitness(self, data_string):
        self.prediksi = self.prediksi_list(data_string)
        temp = []
        for index in range(0, len(data_string)) :
            if data_string[index][-1] == '1' :
                if self.prediksi[index] == True:
                    temp.append(True)
                else:
                    temp.append(False)
            else:
                if self.prediksi[index] == False:
                    temp.append(True)
                else: 
                    temp.append(False)
        self.fitness = temp.count(True) / len(data_string)
#modelss = models(list("111111111111111"))
#modelss.hitung_fitness(nilai_data_latih)
#print(modelss.fitness)

class populasi(object):
    list_individu = []
    ukuran_populasi = None
    kelipatan =[1, 2, 3]
    counter = 0
    no_generasi = 0
    def __init__(self, ukuran_populasi):
        self.ukuran_populasi = ukuran_populasi
        for hitung in range(0, ukuran_populasi):
            gen = random.choice(self.kelipatan)
            temp = []
            for i in range(0, gen*gen_size):
                temp.append(random.choice(['0', '1']))
            self.list_individu.append(models(self.counter,temp))
            self.counter +=1 
            print(self.counter.__len__())
    

        
