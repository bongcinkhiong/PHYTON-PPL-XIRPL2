def luas_balok():
    sidesq = float(input("Side of the Square :"))
    areasq = sidesq * sidesq
    print("Area of the Square : ", areasq)

def luas_segitiga():
    height = float(input("Masukkan nilai tinggi:")) 
    base = float(input(" the Inputase of the triangle :"))
    areatriangle = 0.5 * height * base
    print("Area of the Triangle : ", areatriangle)

def luas_persegipanjang():
    length = float(input("Masukan panjang  Rectangle:  "))
    breadth =float(input("Masukkan luas Rectangle: "))
    arearectangle = length * breadth
    print("Area of the Rectangle : ", arearectangle)

def luas_lingkaran():
    radius = float(input("Input the Radius of The Circle :"))
    areacircle = 3.14 * radius * radius
    print("Area of the Circle : ", areacircle)

print("Select operation.")
print("1.Luas Balok")
print("2.Luas Segitiga")
print("3.Luas Persegi Panjang")
print("4.Luas Lingkaran")

while True:
    choice = input("Masukkan Angka(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan Angka Pertama: "))
        num2 = float(input("Masukkan Angka Kedua: "))

        if choice == '1':
            print(num1, "*", num2, "=", luas_balok(num1, num2))

        elif choice == '2':
            print(0,5, "*", num1, "*", num2, "=", luas_segitiga(0,5,num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", luas_persegipanjang(num1,num2))

        elif choice == '4':
            print(3.14, "*", num1, "*",num2,"=", luas_lingkaran(3.14,num1,num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")