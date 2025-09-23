#include <iostream>
#include "advanced_math.h"
#include "math_utils.h"

using MathUtils::add, MathUtils::multiply, AdvancedMath::square, std::cout, std::endl;

int main(void) {
	int a = 5;
	int b = 7;

	cout << "a + b = " << add(a,b) << endl;
	cout << "a * b = " << multiply(a,b) << endl;
	cout << "square(a) = " << square(a) << endl;

	return 0;
}