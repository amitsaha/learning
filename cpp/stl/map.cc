// map: http://www.cplusplus.com/reference/map/map/
// See: http://www.cplusplus.com/reference/unordered_map/unordered_map/

# include <iostream>
# include <map>
# include <string.h>

int main()
{
  std::map<std::string, int> mymap;
  /* find() returns an iterator */
  std::map<std::string, int>::iterator it;

  mymap["c"] = 67;
  mymap["a"] = 65;
  mymap["b"] = 66;

  it = mymap.find("b");

  /* If the key was not found, it returns an iterator
     to map::end
  */
  if (it != mymap.end())
    std::cout << it->second << std::endl;

  /* To search if a specific key is present, use count()
   */

  /* Maps are sorted by their key
     http://www.cplusplus.com/reference/map/map/key_comp/
   */
  for (it=mymap.begin(); it != mymap.end(); it++)
    std::cout << it->first << it->second << std::endl;  

  return 0;  
}

