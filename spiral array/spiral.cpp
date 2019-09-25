// new reference
#include <iostream>
using namespace std;
main()
{
	int baris, kolom, b = 0;
	cout << "Masukkan Baris ";
	cin >> baris;
	cout << "Masukkan Kolom ";
	cin >> kolom;

	//  a[5][6]
	int a[baris][kolom];

	int atas = 0;
	// bawah = 5 - 1
	int bawah = baris - 1; //bawah=baris-1; untuk menentukan jumlah baris

	int kiri = 0;
	// kanan = 6 - 1
	int kanan = kolom - 1; //kanan=kolom-1; untuk menentukan jumlah kolom

	while (1)
	{
		// 0 > 5
		if (kiri > kanan) //baris atas
			break;
		// looping

		for (int i = kiri; i <= kanan; i++)
			// a[0][0..5] =
			a[atas][i] = b++;
		atas++; // atas = 1

		if (atas > bawah) //kolom kanan
			break;
		for (int i = atas; i <= bawah; i++)
			a[i][kanan] = b++;
		kanan--;

		if (kiri > kanan) //baris bawah
			break;
		for (int i = kanan; i >= kiri; i--)
			a[bawah][i] = b++;
		bawah--;

		if (atas > bawah) //kolom kiri
			break;
		for (int i = bawah; i >= atas; i--)
			a[i][kiri] = b++;
		kiri++;
	}
	cout << endl;

	//output
	for (int i = 0; i < baris; i++)
	{
		for (int j = 0; j < kolom; j++)
		{
			cout << a[i][j] << "\t";
		}
		cout << endl;
	}
}
