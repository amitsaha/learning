# include <iostream>
# include <vector>

int main()
{
  std::vector<int> avec;

  for(int i=0; i<=10;i++) {
    // append to the end
    avec.push_back(i);
  }

  /* Range based for loop, C++11
     g++ -std=c++11  vector.cc
  */
  for(auto elem : avec) {
    std::cout << elem << std::endl;
  }

  return 0;
}   
