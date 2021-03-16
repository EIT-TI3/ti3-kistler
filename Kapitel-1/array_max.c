#include <stdio.h>

// Die eigentliche Lösung der Aufgabe
double max(const double data[], int size) {
    double max = data[0];
    for (int i = 1; i < size; i++) {
        if (data[i] > max) {
            max = data[i];
        }
    }
    return max;
}


// Lediglich zum testen
int main() {
    double test_data[7] = {1.4, 1233.3843, 0.00001, -0.8, -44.3, 1234.0};

    printf("%f", max(test_data, 7));
    return 0;
}
