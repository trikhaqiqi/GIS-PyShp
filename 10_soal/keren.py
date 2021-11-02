# Nama : M. Ilyas Tri Khaqiqi
# NPM : 1194050
# Kelas : D4 - Teknik Informatika 3B
# 1194050 mod 8 = 2 -> membangun bujur sangkar, dan angka 2 terakhir npm = 5, jadi membangun 5 bujur sangkar

import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("brat","satu")
w.record("bret","dua")
w.record("brot","tiga")
w.record("cret","empat")
w.record("crot","lima")

w.poly(parts=[[[11,5],[6.5,5], [6.5,1],[11,1], [11,5]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,5],[5.5,5], [5.5,1],[1,1], [1,5]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[21,1],[12,1], [12,10],[21,10], [21,1]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[11,6],[6.5,6], [6.5,10],[11,10], [11,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,6],[5.5,6], [5.5,10],[1,10], [1,6]]],shapeType=shapefile.POLYLINE)



w.save("soal10")