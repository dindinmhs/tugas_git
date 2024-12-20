data_panen = {
    "lokasi1" : {
        "nama_lokasi" : "Kebun A",
        "hasil_panen" : {
            "padi" : 1200,
            "jagung" : 800,
            "kedelai" : 500,
        }
    },
    "lokasi2" : {
        "nama_lokasi" : "Kebun B",
        "hasil_panen" : {
            "padi" : 1500,
            "jagung" : 900,
            "kedelai" : 450,
        }
    },
    "lokasi3" : {
        "nama_lokasi" : "Kebun C",
        "hasil_panen" : {
            "padi" : 1100,
            "jagung" : 750,
            "kedelai" : 600,
        }
    },
    "lokasi4" : {
        "nama_lokasi" : "Kebun D",
        "hasil_panen" : {
            "padi" : 1300,
            "jagung" : 850,
            "kedelai" : 550,
        }
    },
    "lokasi5" : {
        "nama_lokasi" : "Kebun E",
        "hasil_panen" : {
            "padi" : 1400,
            "jagung" : 950,
            "kedelai" : 480,
        }
    },
}

print(data_panen)

print(data_panen["lokasi2"]["hasil_panen"]["jagung"])
print(data_panen["lokasi3"]["nama_lokasi"])

hasil_kedelai = {}
for k, v in data_panen.items():
    hasil_padi = v["hasil_panen"]["padi"]
    hasil_kedelai = v["hasil_panen"]["kedelai"]
    hasil_jagung = v["hasil_panen"]["jagung"]

    if hasil_padi > 1300 or hasil_jagung > 800:
        print(f"lokasi {v["nama_lokasi"]} memerlukan perhatian khusus")
    else:
        print(f"lokasi {v["nama_lokasi"]} dalam kondisi baik")
    
print("tambah baris baru")