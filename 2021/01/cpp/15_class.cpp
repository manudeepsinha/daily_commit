//small demonstration of class and methods

#include<iostream>

using namespace std;

class BankAccount
{
private:
	float balance;
public:
	BankAccount();
	void Deposit(float);
	void Withdraw(float);
	float getBalance();
	
};

BankAccount::BankAccount()
{
	balance = 0;
}

float BankAccount::getBalance()
{
	return balance;
}

void BankAccount::Deposit(float dep)
{
	balance += dep;
}

void BankAccount::Withdraw(float with)
{
	balance -= with;
	if (balance < 0)
	{
		cout << "You don't have enough balance!" ;
		balance += with;
	}
}

int main()
{
	BankAccount checking;
	BankAccount savings;

	cout << "Checking account balance is: " << checking.getBalance() << endl;
	cout << "Savings account balance is: " << savings.getBalance() << endl;

	checking.Deposit(100)
	savings.Deposit(500)

	cout << "Checking account balance is: " << checking.getBalance() << endl;
	cout << "Savings account balance is: " << savings.getBalance() << endl;

	checking.Withdraw(50)
	savings.Withdraw(1000)

	cout << "Checking account balance is: " << checking.getBalance() << endl;
	cout << "Savings account balance is: " << savings.getBalance() << endl;

	return 0;
}