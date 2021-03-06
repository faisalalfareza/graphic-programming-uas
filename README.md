# Forklift - Simulasi Fungsi
Proyek ini bertujuan untuk membuat pendekatan kecil untuk pemrograman 3D dengan C ++ dan perpustakaan OpenGL. Untuk pengembangan kerangka pengembangan perangkat lunak ini digunakan perpustakaan Qt dan OpenGL. Model dirancang dalam Blender.

## Mengenal Lebih Dalam Tentang Forklift
Forklift adalah mobil berjalan atau kendaraan yang memiliki 2 garpu yang bisa digunakan untuk mengangakat pallet. Biasanya barang diletakkan di atas pallet, baru kemudian barang dipindahkan atau diangkat. Forklift (juga disebut lift truck, jitney, fork truck, fork hoist, atau forklift truck) adalah truk industri yang digunakan untuk mengangkat dan memindahkan material jarak pendek. 

![Screen Shot](https://www.indotara.co.id/inliners/BAGIAN-BAGIAN-FORKLIFT-DAN-FUNGSINYA.png)

Dan untuk perkiraan atau rencana model 3d dari forklift sendiri adalah [seperti pada contoh ini](https://www.google.com/search?q=forklift+opengl+3d&tbm=isch&ved=2ahUKEwjs2ojW5ozjAhXQEysKHU7wCwsQ2-cCegQIABAC&oq=forklift+opengl+3d&gs_l=mobile-gws-wiz-img.12...1130793.1136618..1137785...0.0..0.248.2021.0j5j5......0....1.........0j0i67j0i30.eGKlOP6Z-_k&ei=1VsWXaycDdCnrAHO4K9Y&client=ms-android-samsung-gj-rev1&prmd=isvn&safe=strict).

* **Fork** adalah bagian utama dari forklift yang fungsinya ialah untuk menopang dan untuk membawa serta mengangkat barang atau beban, Fork terbuat dari besi panjang dan lurus dengan panjang standart 1070mm dan bisa di tambah fork extension untuk bisa lebih panjang lagi. Meletakkan beban yang akan di angkat diatas fork harus diperhatikan untuk mengatur lebar fork, perlu diketahui juga dimensi beban dan kapasitas berat beban.
* **Carriage** adalah bagian dari forklift yang sangat penting yang berfungsi sebgai penghubung antara mast dan fork karena ditempat ini fork melekat. Carriage juga berfungsi sebagai sandaran keamanan untuk barang barang di pallet disaat kondisi barang berada di atas mast lifting.
* **Mast** merupakan bagian penting dan utama dari forklift, karena antara fork dan mast adalah satu kesatuan supaya forklift berjalan secara fungsinya. Mast sendiri terbuat dan terdiri dari dua buah besi yang tebal yang di antaranya terdapat komponen hidroulik sistem yang dalam satu kesatuannya berfungsi sebagai pengangkat atau menurunkan barang. Pada dasarnya mast ini fungsinya untuk lifting dan tilting.
* **Overhead Guard** adalah atap atau pelindung untuk operator forklift yang fungsinya adalah melindungi operator jika saat melakukan pekerjaannya dalam mengangkat barang dan barang tersebut jatuh tidak langsung mengenai operator forklift dan jika di modifikasi bisa juga sebagai pelindung operator dari terik matahari dan hujan.
* **Counter Weight** merupakan bagian dari forklift yang fungsingnya menyeimbangkan beban yang diangkat dengan forklift itu sendiri, yang letaknya berada di belakang yang berlawanan dengan fork. Sehingga kesetabilan forklift dan keseimbangannya terjaga.

## Cara Menjalankan 
Proram ini membutuhkan [Python OpenGL (PyOpenGL)](https://anaconda.org/anaconda/pyopengl) dan [Python Imaging library (PIL)](https://anaconda.org/anaconda/pil). Dan untuk mengetahui lebih dalam tentang program ini nantinya, bisa dengan melihat informasi apa saja yang ada didalamnya pada tautan berikut [Forklift - Python OpenGL Information Document](https://github.com/faisalalfareza/graphic-programming-uas/blob/master/Python%20OpenGL%20-%20Information.pdf).

__Run__ Usage: 
```
python main.py
```

# Referensi
* [Objek Forklift Model 3D](https://grabcad.com/library/tag/forklift)

__Working with OpenGL Python__
* [Switch Environment in Python](https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/)
* [Installing Python OpenGL  (PyOpenGL)](https://anaconda.org/anaconda/pyopengl)
* [Installing Python Imaging library (PIL)](https://anaconda.org/anaconda/pil)
* [Installing FreeGlut / GLUT DLL's in Python](https://anaconda.org/conda-forge/freeglut)
