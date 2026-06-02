#include <string>
#include <vector>
#include <sstream>
#include <string_view>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::vector<std::string> stack;
        std::stringstream ss(path);
        std::string part;
        
        // Use stringstream to split by '/'
        while (std::getline(ss, part, '/')) {
            if (part == ".." ) {
                if (!stack.empty()) stack.pop_back();
            } else if (!part.empty() && part != ".") {
                stack.push_back(part);
            }
        }
        
        // Reconstruct path
        std::string result = "";
        for (const std::string& s : stack) {
            result += "/" + s;
        }
        
        return result.empty() ? "/" : result;
    }
};