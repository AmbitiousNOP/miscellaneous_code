#include <iostream>
using namespace std;


int linear_search(int haystack[], int size , int needle){
    for (int i = 0; i < size; i++){
        if (haystack[i] == needle){
            return i;
        }
    }
    return -1;
}

int main(){
    int arr [5] = {1,2,3,4,5};

    cout << linear_search(arr, (sizeof(arr)/4) , 3) << endl;
    cout << linear_search(arr, (sizeof(arr)/4) , 2) << endl;
    cout << linear_search(arr, (sizeof(arr)/4) , 5) << endl;
    cout << linear_search(arr, (sizeof(arr)/4) , 6) << endl;

    return 0;
}