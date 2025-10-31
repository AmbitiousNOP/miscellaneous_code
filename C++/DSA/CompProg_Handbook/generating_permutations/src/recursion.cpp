#include "iostream"
#include "vector"

std::vector<int> permutation;
std::vector<int> chosen;
int n = 3;

void search(){
	if (permutation.size() == n){
		for (auto v: permutation){
			std::cout << v << ' ';
		}
		std::cout << std::endl;
	}else{
		for (int i = 0; i < n; i++){
			if (chosen[i]) continue;
			chosen[i] = true;
			permutation.push_back(i);
			search();
			chosen[i] = false;
			permutation.pop_back();
		}
	}
}

int main(){
	chosen.resize(n);
	search();

	return 0;
}
