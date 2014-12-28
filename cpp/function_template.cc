# include <iostream>

template<class First, class Second, class Third>
Third multiply ( First x, Second y )
{
  return (x * y);
}

int main() {

  double result = multiply<int, int, double> ( 2, 5.5 );
  std::cout << result << std::endl;

  result = multiply<int, double, double> ( 2, 5.5 );
  std::cout << result << std::endl;
  return 0;
}
