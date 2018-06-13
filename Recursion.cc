#include <iostream>
#include <utility>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>


using namespace std;
/*
These functions are for finding he nth number in a finonacci sequence

*/
int nth_fibonacci(int n,int prev,int preprev){
	int curr;
	if (n==0){
	return prev;
	}
	n--;
	curr=prev+preprev;
	return nth_fibonacci(n,curr,prev); 
}

int find_nth_fibonacci(int n){
	return nth_fibonacci(n-1,1,0);
}

/*
This is for counting the number of paths to a destination in a matrix
*/
int count_number_of_paths(pair<int,int>point,int size,map<pair<int,int>,int>mines){
	pair<int,int>down_point,right_point;
	if (point.first>size-1 || point.second>size-1){
		return 0;
	}
	if (mines.count(point)>0){
		return 0;
	}
	
	if (point.first==size-1 && point.second==size-1 ){
		return 1;
	}
	down_point=make_pair(point.first+1,point.second);
	right_point=make_pair(point.first,point.second+1);
	return count_number_of_paths(down_point,size,mines)+count_number_of_paths(right_point,size,mines);
}


int paths_with_mines(int size,map<pair<int,int>,int>mines){
	pair<int,int> starting_point;
	starting_point.first=0;
	starting_point.second=0;
	return count_number_of_paths(starting_point,size,mines);
}


int find_possible_paths(int size){
	map<pair<int,int>,int> mines;
	while (true){
		pair<int,int>input_mine;
		cout<<"Enter Mine corrdinates, Enter -1,-1 to exit \n";
		cin>>input_mine.first>>input_mine.second;
		if (input_mine.first==-1){
			break;
		}
		mines[input_mine]=1;
	}
	return paths_with_mines(size,mines);
}

/*
This is for finding all  possible subsets of a set
*/
void print_path(vector<int> path){
	cout<<" {";
	for (auto it=path.begin();it!=path.end();++it){
		cout<<*it;
		if (it!=path.end()-1)cout<<",";
	}
	cout<<"} ";
}	


void print_all_subsets(vector<int> set,vector<vector<int>> paths_till_now,int position){
	if (position>=set.size())return;

	int curr_element=set[position];
	vector<int>new_path;
	new_path.push_back(curr_element);
	cout<<"{"<<curr_element<<"} ";
	size_t max=paths_till_now.size();
	for(size_t i=0;i<max;i++){
		auto path=paths_till_now[i];
		path.push_back(curr_element);
		print_path(path);
		paths_till_now.push_back(path);
	}
	position++;
	paths_till_now.push_back(new_path);
	print_all_subsets(set,paths_till_now,position);	
}

void find_all_subsets(string strset){
	string delimiter=",";
	vector<int>setelems;
	vector<vector<int>>paths;
	size_t last=0;
	size_t next=0;
	while((next=strset.find(delimiter,last))!=string::npos){
		setelems.push_back(stoi(strset.substr(last,next)));
		last=next+1;
	}
	
	setelems.push_back(stoi(strset.substr(last)));
	print_all_subsets(setelems,paths,0);
}
/*
Generate all possible peremutations of string
*/
//Should replace these vector print functions with one of single template
void print_string(vector<string> perm_string){
	for (auto it=perm_string.begin();it<perm_string.end();++it){
		cout<<*it;
		if (it!=perm_string.end()-1){
			cout<<", ";
		}
	}
}



vector<string> generate_string(string strinput,int position,vector<string>perm_till_now){
	if (position>=strinput.size()){
		return perm_till_now;
	}
	string currletter=string(1,strinput[position]);
	vector<string> return_vec;
	for (string str:perm_till_now){
		for (size_t i=0;i<=str.size();i++)
		{
			string new_str=str.substr(0,i)+currletter+str.substr(i);
			return_vec.push_back(new_str);
		}
	}
	if (position==0){
		return_vec.push_back(currletter);
	}
	return generate_string(strinput,++position,return_vec);
}

void generate_possible_strings(string strinput){
	vector <string> permstring;
	permstring=generate_string(strinput,0,permstring);
	print_string(permstring);
	cout<<"\n";
}
/*
Our aim is to generate all possible valid combinations for brackets. To do this we are going to use binay numbers. Generating combinations can be thought of as generating binay numbers. Where a zero indicates put a ( followed by remaining number of ). 
*/

void print_bracket(int cur_no,int max,const int& size){
	if (cur_no>=max){
		return;
	}
	if (cur_no>0){
		cout<<",";
	}
	bitset<32> cur_no_bitset(cur_no);
	int running_count=0;
	for(int i=0;i<size;i++){
		if (cur_no_bitset[i]==0){
			cout<<"(";
			running_count++;
		}
		else{
			cout<<"()";
			for(int j=running_count;j>0;j--){
				cout<<")";
			}
			running_count=0;
		}
	}
	if (running_count>0){
		for(int j=running_count;j>0;j--){
			cout<<")";
		}
	}
	print_bracket(++cur_no,max,size);
}

void generate_brackets(int number_of_brackets){
	int max=1<<(number_of_brackets-1);
	print_bracket(0,max,number_of_brackets);
}
/*
We show how we can generate a sum using 25,10,5 and 1 cents
*/
int find_possibilities_sum(int sum,vector<int>coins){
	int possibilities=0,current_coin;
	vector<int>coins_next=coins;
	if (coins.size()==1 && coins[0]==1)return 1;
	current_coin=coins.back();
	coins_next.pop_back();
	while(sum>0){
		possibilities+=find_possibilities_sum(sum,coins_next);
		sum-=current_coin;	
	}
	if (sum==0){
		possibilities++;
	}
	return possibilities;
}

int create_given_sum(int sum){
	//Make sure the coins are soroted in descending order.
	vector<int> coins={1,5,10,25};
	return find_possibilities_sum(sum,coins);
}

/*
We can generate all possible configurations
*/


void print_queens_configuration(vector<int> coloumn,int size){
	for (int col :coloumn){
		for (int i=0;i<size;i++){
			if (i==col){
				cout<<"[X]";
			}
			else{
				cout<<"[ ]";
			}
		}
		cout<<"\n";
	}
	cout<<"----------------------";
	cout<<"\n\n";
}

bool check_if_valid(vector<int> coloumn,int curr_pos){
	for (int i=0;i<coloumn.size();i++){
		if (coloumn[i]==curr_pos){
			return false;
		}
		//cout<<"curr pos : "<<i<<" Col_val : "<<coloumn.size()<<" Diff : "<<i-(int)coloumn.size()<<" Abs : "<<abs(i-(int)coloumn.size())<<endl;
		int diff_l=abs(coloumn[i]-curr_pos);
		int diff_r=abs(i-(int)coloumn.size());
		//cout<<"Difference values : "<<diff_l<<diff_r<<endl;
		if (diff_l==diff_r){
			return false;
		}
	}
	return true;
}


int solve_eight_queen_problem(vector<int> coloumn,int size,bool print_configs){
	int possibilities=0;
	if (coloumn.size()==size){
		if (print_configs)print_queens_configuration(coloumn,size);
		return 1;		
	}	
	for (int i=0;i<size;i++){
		if (check_if_valid(coloumn,i)){
			vector<int>new_config(coloumn);
			new_config.push_back(i);
			possibilities+=solve_eight_queen_problem(new_config,size,print_configs);	
		}
	}
	return possibilities;
}

int possible_combinations(int size,bool print_configs){
	vector<int> coloumn;
	return solve_eight_queen_problem(coloumn,size,print_configs);		
}
//Fuctinos common to all questions
void print_menu(){	
		cout<<"\n================================================\n";
		cout<<"We have a set of programs that deal with recusion"<<endl;
		cout<<"-------------------------------------------------"<<endl;
		cout<<"The Following are the options : \n\n";
		cout<<string(5,' ')<<"1.Nth Fibonacci Number\n";
		cout<<string(5,' ')<<"2.Possible paths in square\n";
		cout<<string(5,' ')<<"3.Generate all subsets of set\n";
		cout<<string(5,' ')<<"4.Compute all permutataions \n";
		cout<<string(5,' ')<<"5.Compute all Valid brackets\n";
		cout<<string(5,' ')<<"6.Create sum using 25,10,5 and 1 cents\n";
		cout<<string(5,' ')<<"7.8 Queens possible combinations\n";
		cout<<string(4,' ')<<"-1 Exit\n\n";
		cout<<string(2,' ')<<"Enter your choice \n";

}



int main(){
	int choice;
	string strinput;
	while (true){
		print_menu();
		cin>>choice;
		switch(choice){
			case 1:
				int n,paths;
				cout<<"We are going to find the nth fibonacci number\n";
				cout<<"Enter a value for n \n";
				cin>>n;
				cout<<"Nth fibonacci number is : "<<find_nth_fibonacci(n)<<endl;
				continue;
			case 2:	
				cout<<"We are going to find the possible paths to move from (0,0) to (n,n), when you can only move right and down\n";
				cout<<"We are going to first get the input for the size of square and second we are going to get input for size of square\n";
				cout<<"Input size of square \n";
				cin>>n;
				paths=find_possible_paths(n);
				cout<<"Number of Possible Paths : "<<paths<<endl;
				continue;			
			case 3:
				cout<<"We are going to generate all subsets of a set, so enter the elements of set seperate by ,\n";
				cin>>strinput;
				find_all_subsets(strinput);
				cout<<"\n";
				continue;
			case 4:
				cout<<"We are going to create all possible permutations of a given string\n";
				cout<<"Enter string \n";
				cin>>strinput;
				generate_possible_strings(strinput);					
				continue;
			case 5:
				cout<<"We are going to generate all possible combinations of brackets(question 8.5) \n";
				cout<<"Enter the number of brackets \n"	;
				cin>>n;
				generate_brackets(n);
				continue;
			case 6:
				cout<<"We are going to show the number of ways of representing N cents, using 25 cents,10 cents,5 cents and 1 cent\n";
				cout<<"Enter the amount that needs to be formed\n";
				cin>>n;
				cout<<"We can create the sum : "<<create_given_sum(n)<<" ways \n";
				continue;
			case 7:
				cout<<"8 Queens Problem. We are going to print all possible configurations\n";
				cout<<"We are going to show all possible ways in which 8 queen problem can be solved\n";
				cout<<"Enter size of the board\n";
				cin>>n;
				n=possible_combinations(n,true);
				cout<<"Possible combinations : "<<n<<endl;
				continue;	
			case -1:
				break;
			default:
				cout<<"Invalid Option\n";
			
				
		}
		
		
	return 0;


	}
}
