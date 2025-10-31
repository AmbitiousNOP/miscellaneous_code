#include <iostream>
#include <vector>


std::vector<int> subset;

void search(int k, int n){
	if (k == n){
		// process subset
		for (auto i: subset){
			std::cout << i << ' ';
		}
		std::cout << std::endl;
	}
	else{
		search(k+1, n);
		subset.push_back(k);
		search(k+1, n);
		subset.pop_back();
	}


}



int main(){

	search(0, 3);
	return 0;
}
