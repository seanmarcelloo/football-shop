Link aplikasi PWS: https://sean-marcello-footballshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

Pertama buat dahulu direktori lokal untuk proyek saya, lalu melakukan inisiasi dengan git init.
Lalu buat repositori daring di github beserta branch utama dan menghubungkan kedua repositori tersebut dengan menambahkan remote. 
Selanjutnya saya membuat virtual env dan membuat berkas pada requiirements.txt yang berisi dependencies yang digunakan pada proyek, lalu menginstallnya pada v env. Barulah saya membuat proyek Dango baru saya yang berjudul football-shop. Di sana saya juga mengatur env variables, production configuration, dan settings. 

Selanjutnya, saya membuat aplikasi dengan nama main dengan "python manage.py startapp main" dan menambahkan 'main' pada INSTALLED_APPS di settings.py.

Setelah itu, saya membuat model pada aplikasi main dengan nama class Product dan menambahkan keenam atribut yang diminta beserta tipenya. Saya juga menambahkan CATEGORY_CHOICES yang sesuai dengan konteks proyek saya dan magic method yang mereturn nama produk untuk mendefine representasi string pada model.

Pada views.py, saya membuat berkas main.html yang menampilkan nama aplikasi, nama, dan kelas saya lalu menambahkan fungsi dengan nama show_main yang berisi data yang say tampilkan pada berkas main.html.

Saya melakukan routing dengan membuat konfigurasi routing untuk aplikasi main pada berkas urls.py di direktori main, lalu saya tambahkan url tersebut pada url tingkat proyek, sehingga aplikasi main dapat dijalankan.

Akhirnya, saya melakukan deployment melalui pws dengan membuat proyek baru pada pws, menyimpan credentials. Pada environs dan melakukan kofnigurasi project env variables sesuai yang sudah saya buat sebelumnya. Lalu saya menambahkan url deployemnt pada pws dan akhirnya melakukan add, commit, dan push pada git.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![bagan](download.png)

Penjelasan:

Saat pengguna mengakses aplikasi Django melalui sebuah URL, permintaan tersebut diproses oleh arsitektur MVT, di mana URL mapper (urls.py) akan mencocokkan alamat yang diminta dan meneruskannya ke View yang tepat. Jika view yang sesuai ditemukan, maka view tersebut akan dipanggil untuk memproses permintaan. Dalam prosesnya, View dapat berinteraksi dengan Model untuk mengambil data yang diperlukan dari database. Setelah data berhasil diambil, View akan memanfaatkan Template untuk merender halaman dengan menyisipkan data tersebut ke dalam HTML, lalu hasil akhirnya dikirim kembali ke pengguna dalam bentuk respon.

referensi: https://www.educative.io/answers/what-is-mvt-structure-in-django


3. Jelaskan peran settings.py dalam proyek Django!
Dalam proyek Django, berkas settings.py berfungsi sebagai pusat pengaturan yang mengatur bagaimana aplikasi dijalanakan. Di dalamnya terdapat berbagai kofnigurasi, seperti jenis basis data yang digunakan (pada DATABASES), daftar aplikasi yang diaktifkan pada proyek (pada INSTALLED_APPS), serta pengaturan keamanan seperti SECRET_KEY dan ALLOWED_HOSTS.
Secara garis besar, settings.py menjadi pusat konfigurasi yang memastikan setiap komponen dalam proyek Django dapat bekerja sesuai kebutuhan, baik dalam tahap pengembangan maupun ketika dijalankan di lingkungan produksi.

4. Bagaimana cara kerja migrasi database di Django?
Migrasi dilakukan untuk menyesuaikan perubahan pada model di models.py dengan struktur tabel di database. Ketika sebuah model diinisiasi atau dimodifikasi, perintah python manage.py makemigrations akan menghasilkan file migrasi yang berisi instruksi mengenai perubahan tersebut. Kemudian,pada perintah python manage.py migrate, instruksi tersebut dijalankan dan diterjemahkan menjadi perintah SQL yang sesuai sehingga database diperbarui. Django juga mencatat setiap migrasi yang sudah dilakukan dalam tabel django_migrations, sehingga sistem dapat mengetahui bagian mana yang sudah sinkron.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan framework pertama dalam pembelajaran pengembangan perangkat lunak karena fiturnya yang lengkap dan mudah dipahami. Django telah menyediakan berbagai kebutuhan dasar seperti routing, autentikasi, dan pengelolaan basis data, sehingga kita tidak perlu membangun semuanya dari awal. Strukturnya yang menggunakan Model–Template–View membantu memisahkan bagian data, logika, dan tampilan secara jelas. Selain itu, Django menggunakan bahasa Python yang memiliki sintaks sederhana sehingga lebih mudah dipelajari oleh mahasiswa. Ditambah lagi, dokumentasinya sangat baik, komunitasnya luas, serta banyak digunakan di industri besar, sehingga pembelajaran Django tidak hanya memperkenalkan dasar pengembangan web, tetapi juga membiasakan mahasiswa dengan praktik terbaik yang sesuai dengan kebutuhan dunia kerja.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? tidak ada hehe