data = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

def putarList(listbalik):
    data_spin = [[], [], []]
    for i in range(len(listbalik)):
        for j in range(len(listbalik)):
            data_spin[i].append(listbalik[(len(listbalik)- 1) -j][i])
    return data_spin

print(putarList(data))

#Maaf mas, soal nomor 2 dan nomor 3 saya juga nyerah
