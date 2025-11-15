#include <iostream>
#include <cmath>
using namespace std;

int bin_search(int haystack [], int length ,int needle){
    int low = 0;
    int high = (length/4)-1;
    while(low < high){
        int mid_point = floor(low + (high-low) / 2);
        int value = haystack[mid_point];

        if (value == needle){
            return 1;
        }else if (value > needle){
            high = mid_point;
        }else if (value < needle){
            low = mid_point + 1;
        }
    }

    return 0;

}


int main(){

    int arr [] = {1,2,3,4,5,6,7,8,9,10};

    cout << bin_search(arr, sizeof(arr), 8) << endl;
    cout << bin_search(arr, sizeof(arr), 1) << endl;
    cout << bin_search(arr, sizeof(arr), 52) << endl;
    return 0;
}