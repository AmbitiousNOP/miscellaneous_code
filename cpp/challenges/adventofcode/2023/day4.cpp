#include <iostream>
#include <fstream>
using namespace std;

struct scratch_off{
    string game_id;
    int winning_nums[4]; // Needs to be changed after testing
    int my_cards[8]; // Needs to be changed after testing
};

int main(){
    string line;
    ifstream data_file ("example_data.txt");
    if (data_file.is_open()){
        while (getline(data_file,line)){
            //string test_num = (line.substr(0, line.find("|"))).substr(line.find(":")+1);
            string my_cards = line.substr(line.find("|") + 1, line.find("\n"));
            
            for (int c = 0; c < my_cards.length(); c++){
                if (isdigit(my_cards[c])){
                    cout << my_cards[c];
                }else{
                    cout << "\n";
                }
            }
            

            
        }
        data_file.close();
    }
    else cout << "unable to open file" << endl;

    


    return 0;
}