#include "iostream"
#include "vector"
#include "algorithm"

int main(){
	std::vector<int> permutation;
	int n = 3;

	for (int i = 0; i < n; i++){
		permutation.push_back(i);
	}

	do {
		for (int v: permutation){
			std::cout << v << ' ';
		}
		std::cout << std::endl;
	}while (std::next_permutation(permutation.begin(), permutation.end()));


	return 0;

}
