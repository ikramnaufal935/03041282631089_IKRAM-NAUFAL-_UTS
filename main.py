data_level = [18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15,
              0, 30, 80, 81, 100]

def status_level(level):
    if level < 30:
        return "LOW"

    elif level <= 80:
        return "NORMAL"

    else:
        return "HIGH"


def hitung_kategori(data):
    jumlah = {
        "LOW": 0,
        "NORMAL": 0,
        "HIGH": 0
    }

    for level in data:
        status = status_level(level)
        jumlah[status] += 1

    return jumlah

def rata_rata(data):
    total = sum(data)
    return total / len(data)

def tampilkan_monitoring(data):

    print("\n========================================")
    print("       HASIL MONITORING LEVEL TANGKI")
    print("========================================")

    for i, level in enumerate(data, start=1):

        status = status_level(level)

        print(
            f"Data {i:02d} | "
            f"Level = {level}% | "
            f"Status = {status}"
        )

def tampilkan_ringkasan(data):

    jumlah = hitung_kategori(data)

    rata = rata_rata(data)
    maksimum = max(data)
    minimum = min(data)

    print("\n========================================")
    print("             RINGKASAN DATA")
    print("========================================")

    print("Total Data       :", len(data))
    print("Jumlah LOW       :", jumlah["LOW"])
    print("Jumlah NORMAL    :", jumlah["NORMAL"])
    print("Jumlah HIGH      :", jumlah["HIGH"])

    print("----------------------------------------")

    print(f"Rata-rata Level  : {rata:.2f}%")
    print(f"Level Maksimum   : {maksimum}%")
    print(f"Level Minimum    : {minimum}%")

    print("========================================")

def uji_program():

    data_uji = [
        (29, "LOW"),
        (30, "NORMAL"),
        (31, "NORMAL"),
        (79, "NORMAL"),
        (80, "NORMAL"),
        (81, "HIGH"),
        (0, "LOW"),
        (100, "HIGH")
    ]

    print("\n========================================")
    print("             TESTING PROGRAM")
    print("========================================")

    berhasil = 0

    for i, (nilai, expected) in enumerate(data_uji, start=1):

        actual = status_level(nilai)

        if actual == expected:
            hasil = "PASS"
            berhasil += 1
        else:
            hasil = "FAIL"

        print(
            f"Test {i} | "
            f"Input = {nilai}% | "
            f"Expected = {expected} | "
            f"Actual = {actual} | "
            f"Hasil = {hasil}"
        )

    print("----------------------------------------")
    print(f"Total Testing : {len(data_uji)}")
    print(f"Berhasil      : {berhasil}")
    print(f"Gagal         : {len(data_uji) - berhasil}")
    print("========================================")

def main():

    print("========================================")
    print("       MONITORING LEVEL TANGKI")
    print("       KELOMPOK C - INSTRUMENTASI")
    print("========================================")

    print("Jumlah data:", len(data_level))

    tampilkan_monitoring(data_level)

    tampilkan_ringkasan(data_level)

    uji_program()


if __name__ == "__main__":
    main()

