/* Split a string into a vector of strings
   Taken from: http://stackoverflow.com/questions/236129/split-a-string-in-c
 */
#include <string>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

vector<string> split(const string &s, char delim) {
  vector<string> elems;
  stringstream ss(s);
  string item;
  while (std::getline(ss, item, delim)) {
    if (!item.empty())
      elems.push_back(item);
  }
  return elems;
}

int main(int argc, char **argv)
{
  vector<string> elems = split(argv[1],',');
  for(int i=0; i<elems.size(); i++)
    cout << elems[i] << endl;
  return 0;
}
