#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){    
    string line; 
    ifstream data_file ("puzzle_input.txt");
    vector <char> buffer;
    int sum = 0; 

    if (data_file.is_open()){
        while (getline(data_file, line)){
            for (int i = 0; i < line.length(); i++){
                if (isdigit(line[i])){
                    buffer.push_back(line[i]);
                    
                }
            }
            string str_nums;
            str_nums += buffer[0];
            str_nums += buffer.back();
            sum += stoi(str_nums);
            buffer.clear();
        }
    }
    else{
        cout << "Unable to open file" << endl;
    }
    data_file.close();

    cout << sum << endl;


    return 0;
}