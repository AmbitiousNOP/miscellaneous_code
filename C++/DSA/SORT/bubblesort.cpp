#include <iostream>
using namespace std;


int bubble_sort(int haystack [], int length){
    /* For future experiments: can this be done in place? without the use of temp_variable*/
    for(int i = 0; i <= length/4-2; i++){
        if (haystack[i] > haystack[i+1]){
            int temp_variable = haystack[i];
            haystack[i] = haystack[i+1];
            haystack[i+1] = temp_variable;
            i = -1;
        }
    }
    return 0;

}

int main(){
    int arr[] = {1,2,4,22,5,6,7,8,9,11,10,13,12,14,15};

    cout << "Before Bubble Sort: " << endl;
    for(int i = 0; i <= sizeof(arr)/4-1; i++){
        cout << arr[i] << " ";
    }

    cout << endl << "After Bubble Sort: " << endl;
    bubble_sort(arr, sizeof(arr));
    for(int i = 0; i <= sizeof(arr)/4-1; i++){
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}

