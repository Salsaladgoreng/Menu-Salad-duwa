from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="salad_db"
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil_pencarian = None
    pesan_error = None
    kata_kunci = ""

    if request.method == "POST":
        kata_kunci = request.form.get('search_query', '')

        if kata_kunci:
            try:
                db = get_db_connection()
                cursor = db.cursor(dictionary=True)

                query = "SELECT * FROM data_kota WHERE nama LIKE %s"
                cursor.execute(query, (f"%{kata_kunci}%",))
                
                hasil_pencarian = cursor.fetchone()
                
                cursor.close()
                db.close()
                
                if not hasil_pencarian:
                    pesan_error = f"Maaf, informasi tentang '{kata_kunci}' belum tersedia."
            except Exception as e:
                print(f"Error: {e}")
                pesan_error = "Maaf, terjadi kesalahan pada koneksi database."
        
    return render_template('index.html', hasil=hasil_pencarian, error=pesan_error, query=kata_kunci)

if __name__ == '__main__':
    app.run(debug=True)