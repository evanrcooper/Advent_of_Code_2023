#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main() {

    int count = 0;

    int maxRed = 12;
    int maxGreen = 13;
    int maxBlue = 14;

    fstream file;
    file.open("input.txt");

    if (!file.is_open()) {
        cerr << "File Does Not Exist";
    }

    string line, color, amount, game;

    while (getline(file, line)) {

        int curRed = 0;
        int curGreen = 0;
        int curBlue = 0;

        stringstream buffer(line);
        
        buffer >> game;
        buffer >> game;
        
        bool brk = false;

        do {

            buffer >> amount;
            buffer >> color;

            // cout << amount << " - " << game.substr(0, game.length() - 1) << "\n";

            switch (color[0]) {
                case 'r':
                    if (stoi(amount) > maxRed) {
                        count += stoi(game.substr(0, game.length() - 1));
                        brk = true;
                        cout << game.substr(0, game.length() - 1) << "r\n";
                    }
                    break;

                case 'g':
                    if (stoi(amount) > maxGreen) {
                        count += stoi(game.substr(0, game.length() - 1));
                        brk = true;
                        cout << game.substr(0, game.length() - 1) << "g\n";
                    }
                    break;

                case 'b':
                    if (stoi(amount) > maxBlue) {
                        count += stoi(game.substr(0, game.length() - 1));
                        brk = true;
                        cout << game.substr(0, game.length() - 1) << "b\n";
                    }
                    break;

                default:
                    cerr << "Invalid Color";

            }

        } while ((!brk) && (color[color.length()-1] == ',' || color[color.length()-1] == ';'));
    }

    int total = 0;
    for (int i = 1; i <= 100; i++) {
        total += i;
    }

    cout << total - count;

    file.close();
}