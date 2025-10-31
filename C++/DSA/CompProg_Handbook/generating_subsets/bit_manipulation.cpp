#include "iostream"
#include "vector"








int main(){
	int n = 3;
	for (int b=0; b < (1<<n);b++){
		std::vector<int> subset;
		for (int i=0; i < n; i++){
			if (b&(1<<i)){
				subset.push_back(i);
			}
		}
		for (auto e: subset){
			std::cout << e << ' ';
		}
		std::cout << std::endl;

	}

	return 0;
}
