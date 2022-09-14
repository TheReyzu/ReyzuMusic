HELP_1 = """✅**<u>Admin Commands :</u>**

**c** singkatan untuk putar di Channel.

/pause or /cpause - Jeda musik yang diputar.
/resume or /cresume - Lanjutkan musik yang dijeda.
/mute or /cmute - Bisukan musik yang diputar.
/unmute or /cunmute - Suarakan musik yang dibisukan.
/skip or /cskip - Lewati musik yang sedang diputar.
/stop or /cstop - Hentikan pemutaran musik.
/shuffle or /cshuffle - Secara acak mengacak daftar putar yang antri.
/seek or /cseek - Teruskan mencari musik sesuai durasi.
/seekback or /cseekback - Kembali mencari musik sesuai durasi.
/restart - Mulai ulang Bot untuk grup Anda.


✅<u>**Specific Skip :**</u>
/skip or /cskip [Nomor (contoh : 3)] 
    - Melewati musik ke nomor antrian yang ditentukan. Contoh : /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Loop Play :**</u>
/loop or /cloop [enable/disable] or [Angka antara 1-10] 
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara.

✅<u>**Auth Users :**</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Username] - Tambahkan pengguna ke daftar AUTH grup.
/unauth [Username] - Hapus pengguna dari daftar AUTH grup.
/authusers - Periksa daftar AUTH grup."""


HELP_2 = """✅<u>**Play Commands :**</u>

Perintah yang tersedia = play , vplay , cplay

Perintah ForcePlay = playforce , vplayforce , cplayforce

**c** singkatan dari pemutaran Channel.
**v** singkatan dari pemutaran video.
**force** singkatan dari force play.

/play or /vplay or /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

/playforce or /vplayforce or /cplayforce -  **Force Play** menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrean.
/channelplay [Chat username or id] or [Disable] - Hubungkan channel ke grup dan streaming musik di obrolan suara channel dari grup Anda.


✅**<u>Bot's Server Playlists :</u>**
/playlist  - Periksa Daftar Putar tersimpan Anda di server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda.
/play  - Mulai mainkan Daftar Putar tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Bot Commands :**</u>

/stats - Dapatkan Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat, dll.

/sudolist - Periksa Pengguna Sudo

/lyrics [Nama Musik] - Mencari Lirik untuk Musik tertentu di web.

/song [Nama Trek] or [YT Link] - Unduh lagu apa pun dari youtube dalam format mp3 atau mp4.

/player -  Dapatkan Panel Mainkan interaktif.

**c** singkatan dari pemutaran saluran.

/queue or /cqueue - Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Extra  Commands :**</u>
/start - Memulai Bot.
/mhelp  - Dapatkan Menu  Perintah dengan penjelasan rinci tentang perintah.
/ping - Ping Bot dan periksa statistik Ram, Cpu, dll dari Bot.

✅<u>**Group Settings :**</u>
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris.

🔗 **Opsi Pengaturan :**

1️⃣ Anda dapat mengatur **Kualitas Audio** yang ingin Anda streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** yang ingin Anda streaming di obrolan suara.

3️⃣ **Auth Users** : - Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang hadir di grup Anda akan dapat menggunakan perintah admin (seperti /skip, /stop dll)

4️⃣ **Clean Mode :** Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Command Clean** : Saat diaktifkan, Bot akan segera menghapus perintah yang dijalankannya (/play, /pause, /shuffle, /stop dll).

6️⃣ **Play Settings :**

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol tempat Anda dapat mengatur pengaturan pemutaran grup Anda. 

<u>Options in playmode :</u>

1️⃣ **Search Mode** [Direct atau Inline] - Mengubah mode pencarian Anda saat Anda memberikan mode /play. 

2️⃣ **Admin Commands** [Everyone atau Admins] - Jika Everyone, siapa pun yang hadir di grup Anda akan dapat menggunakan perintah admin (seperti /skip, /stop dll).

3️⃣ **Play Type** [Everyone atau Admins] - Jika admins, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username atau Balas ke Pengguna]
/delsudo [Username atau Balas ke Pengguna]

🛃**<u>HEROKU :</u>**
/usage - Penggunaan Dynos.

🌐**<u>CONFIG VARS :</u>**
/get_var - Dapatkan var konfigurasi dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Nama Var] [Value] - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Value dengan spasi.

🤖**<u>BOT COMMANDS :</u>**
/reboot - Nyalakan ulang Bot. 
/update - Perbarui Bot.
/speedtest - Periksa kecepatan server
/maintenance [enable / disable] 
/logger [enable / disable] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Number of Lines] - Dapatkan log bot Anda dari heroku atau vps. Bisa untuk keduanya.
/autoend [enable|disable] - Aktifkan Auto end setelah 3 menit jika tidak ada yang mendengarkan.

📈**<u>STATS COMMANDS :</u>**
/activevoice - Periksa obrolan suara aktif di Bot.
/activevideo - Periksa panggilan video aktif di Bot.
/stats - Periksa Statistik Bot.

⚠️**<u>BLACKLIST CHAT FUNCTION :</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan Grup.
/whitelistchat [CHAT_ID] - Mengubah daftar hitam ke daftar putih obrolan grup
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION :</u>**
/block [Username atau Balas ke Pengguna] - Mencegah pengguna menggunakan perintah Bot.
/unblock [Username atau Balas ke Pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

👤**<u>GBAN FUNCTION :</u>**
/gban [Username atau Balas ke Pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan Bot.
/ungban [Username atau Balas ke Pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan Bot.
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥**<u>VIDEOCALLS FUNCTION :</u>**
/set_video_limit [Number atau Chats] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode download diaktifkan, Bot akan mengunduh video. Bot Secara default ke M3u8. Anda dapat menggunakan mode unduhan ketika kueri apa pun tidak diputar dalam mode m3u8.

⚡️**<u>PRIVATE BOT FUNCTION :</u>**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan Bot.
/unauthorize [CHAT_ID] - Larang obrolan menggunakan Bot.
/authorized - Periksa semua obrolan Bot yang dizinkan.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message atau balas ke pesan] - Siarkan pesan apa pun ke Grup yang Dilayani Bot.

<u>options for broadcast :</u>
**-pin** : Menyematkan pesan Anda
**-pinloud** : Menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Menyiarkan pesan Anda ke pengguna yang telah memulai Bot.
**-assistant** : Menyiarkan pesan Anda dari akun asisten Bot.
**-nobot** : Memaksa Bot untuk tidak menyiarkan pesan.

**Contoh :** `/broadcast -user -assistant -pin Ayang Melati`

"""
