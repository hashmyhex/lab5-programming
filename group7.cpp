#include <iostream>
#include <iomanip>
#include <windows.h> // кодировка с смд шиндоус

int main() {
    // утф-8 для работы внутри консоли у нейронки спросил
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);

    int n;
    std::cout << "введите N: ";
    if (!(std::cin >> n)) {
        std::cout << "ошибка!!! надо только цифры\n";
        return 0;
    }

    if (n < 1) {
        std::cout << "N должно быть больше 0\n";
        return 0;
    }

    double total = 0;
    for (int i = 1; i <= n; ++i) {
        total += 1.0 / i;
    }
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "сумма ряда при N == " << n << ": " << total << "\n";
    return 0;
}
