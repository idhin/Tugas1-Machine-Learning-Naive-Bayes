import pandas as pd

# Baca TrainSet dan TestSet
Train = pd.read_csv('TrainsetTugas1ML.csv')
Test = pd.read_csv('TestsetTugas1ML.csv')


# Kita buat fungsinya
def count(lab1, value1, lab2,
          value2):
    i = 0
    for j in range(len(Train)):
        if (Train[lab1][j] == value1) & (Train[lab2][j] == value2):
            i = i + 1
    return i

#Kita hitung peluangnya menggunakan naive bayes
def naivebayes(lab1, value1, lab2, value2, income_type):
    result = count(lab1, value1, lab2, value2) / income_type
    return result

# Langkah Pertama Kita Tentukan Peluang Incomenya -> >50K dan <=50K
big_income = 0  # ngitung banyak income >50K
small_income = 0  # ngitung banyak income <=50K
for a in range(len(Train)):
    if (Train['income'][a] == '>50K'):
        big_income = big_income + 1
    else:
        small_income = small_income + 1
Pelbig_income = big_income / len(Train)
Pelsmall_income = small_income / len(Train)

# Langkah Kedua Kita Tentukan Peluang Dari Masing-Masing Atribut
income = []
for i in range(len(Test)):
    PelageBig = naivebayes('age', Test['age'][i], 'income', '>50K', big_income)
    PelageSmall = naivebayes('age', Test['age'][i], 'income', '<=50K', small_income)

    PelworkclassBig = naivebayes('workclass', Test['workclass'][i], 'income', '>50K', big_income)
    PelworkclassSmall = naivebayes('workclass', Test['workclass'][i], 'income', '<=50K', small_income)

    PeleducationBig = naivebayes('education', Test['education'][i], 'income', '>50K', big_income)
    PeleducationSmall = naivebayes('education', Test['education'][i], 'income', '<=50K', small_income)

    PelmaritalstatusBig = naivebayes('marital-status', Test['marital-status'][i], 'income', '>50K', big_income)
    PelmaritalstatusSmall = naivebayes('marital-status', Test['marital-status'][i], 'income', '<=50K', small_income)

    PeloccupationBig = naivebayes('occupation', Test['occupation'][i], 'income', '>50K', big_income)
    PeloccupationSmall = naivebayes('occupation', Test['occupation'][i], 'income', '<=50K', small_income)

    PelrelationshipBig = naivebayes('relationship', Test['relationship'][i], 'income', '>50K', big_income)
    PelrelationshipSmall = naivebayes('relationship', Test['relationship'][i], 'income', '<=50K', small_income)

    PelhoursperweekBig = naivebayes('hours-per-week', Test['hours-per-week'][i], 'income', '>50K', big_income)
    PelhoursperweekSmall = naivebayes('hours-per-week', Test['hours-per-week'][i], 'income', '<=50K', small_income)

    Pup = PelageBig * PelworkclassBig * PeleducationBig * PelmaritalstatusBig * PeloccupationBig * PelrelationshipBig * PelhoursperweekBig * Pelbig_income
    Pdown = PelageSmall * PelworkclassSmall * PeleducationSmall * PelmaritalstatusSmall * PeloccupationSmall * PelrelationshipSmall * PelhoursperweekSmall * Pelsmall_income
    
# Selanjutnya Hasil yang Sudah Kita Prediksikan Ditampung dalam Datatest_Income
    if (Pup > Pdown):
        income.append('>50K')
    else:
        income.append('<=50K')

# Terakhir Kita Masukkan Hasil Prediksi Kedalam File Datatest
for k in range(len(Test)):
    age = [];
    workclass = [];
    education = [];
    marital = [];
    occupation = [];
    relationship = [];
    hours = [];
    age.append(Test['age'][k])
    workclass.append(Test['workclass'][k])
    education.append(Test['education'][k])
    marital.append(Test['marital-status'][k])
    occupation.append(Test['occupation'][k])
    relationship.append(Test['relationship'][k])
    hours.append(Test['hours-per-week'][k])

#Tampil dan Cetak Hasilnya
print(income)
output = pd.DataFrame(
    {'age': age, 'workclass': workclass, 'education': education, 'marital-status': marital, 'occupation': occupation,
     'relationship': relationship, 'hours-per-week': hours, 'income': income}, index=Test['id'])
output.to_csv("TebakanTugas1ML.csv") # Mengeluarkan output TebakanTugas1ML.csv

