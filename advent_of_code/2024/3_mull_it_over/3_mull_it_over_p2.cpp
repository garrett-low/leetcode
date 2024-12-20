#include <algorithm>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

void read_file(std::string_view filename, std::vector<std::string> &input);

int main(int argc, char **argv) {
  if (argc != 2) {
    perror("Specify an input file!");
    return 1;
  }

  std::string filename = argv[1];

  std::vector<std::string> input;
  read_file(filename, input);
  // std::cout << input << '\n';

  int score{};
  bool is_enabled = true;

  for (int ln = 0; ln < input.size(); ln++) {
    std::string instr = input[ln];
    // std::cout << instr << '\n';
    for (int i = 0; i < instr.length() - 3; i++) {
      std::string op{instr.substr(i, 3)};
      // std::cout <<  op << '\n';
      if (op == "mul") {
        // std::cout << op << '\n';

        i = i + 2;

        if (!is_enabled) {
          continue;
        }

        char curr = instr[++i];
        if (curr != '(') {
          continue;
        }

        curr = instr[++i];
        std::string first_operand{};
        while (std::isdigit(curr) && i < instr.length()) {
          first_operand += curr;
          curr = instr[++i];
        }
        // std::cout << first_operand << '\n';

        if (first_operand.empty() ||
            !std::all_of(first_operand.begin(), first_operand.end(),
                         ::isdigit)) {
          continue;
        }

        // std::cout << "after first_op: " << curr << '\n';
        if (curr != ',') {
          continue;
        }

        std::string sec_operand{};
        curr = instr[++i];
        while (std::isdigit(curr) && i < instr.length()) {
          sec_operand += curr;
          curr = instr[++i];
        }
        // std::cout << sec_operand << '\n';

        if (sec_operand.empty() ||
            !std::all_of(sec_operand.begin(), sec_operand.end(), ::isdigit)) {
          continue;
        }

        if (curr != ')') {
          continue;
        }

        int first_op = std::stoi(first_operand);
        int sec_op = std::stoi(sec_operand);

        // std::cout << "first_op: " << first_op << '\n'
                  // << ", second op: " << sec_op << '\n';
        // if (!is_enabled) {
        //   continue;
        // }
        score += (first_op * sec_op);
      }

      if (i + 4 >= instr.length()) {
        continue;
      }
      op = instr.substr(i, 4);
      if (op == "do()") {
        is_enabled = true;
        i = i + 3;
        // std::cout << is_enabled << '\n';
        continue;
      }

      if (i + 7 >= instr.length()) {
        continue;
      }
      op = instr.substr(i, 7);
      if (op == "don't()") {
        is_enabled = false;
        i = i + 6;
        // std::cout << is_enabled << '\n';
        continue;
      }
    }
  }
  // std::cout << '\n';
  std::cout << "P2: " << score << '\n';
}

void read_file(std::string_view filename, std::vector<std::string> &input) {
  std::string file{filename};
  std::ifstream ifs(file);
  if (!ifs) {
    perror("Couldn't open file!");
    return;
  }

  std::string instr;
  while (std::getline(ifs, instr)) {
    input.push_back(instr);
    // std::cout << instr << '\n';
  }
}
