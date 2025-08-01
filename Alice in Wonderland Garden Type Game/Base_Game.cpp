#include <iostream>
using namespace std;

int main() {
    bool gameRunning = true;

    while (gameRunning) {
        cout << "\n=============================\n";
        cout << "   ITEM RECOVERY\n";
        cout << "=============================\n";
        cout << "1. Play\n";
        cout << "2. Quit Game\n";
        cout << "Choose an option: ";

        int choice;
        cin >> choice;

        if (choice == 1) {
            cout << "\nJuly 31, Thursday, 11:42 am.\n";
            cout << "\nLiving Room\n";
            cout << "\n \n";
            cout << "\nYou have 18 minutes to get to work.\n";
            cout << "\nHowever, you are missing 3 essential items.\n";
            cout << "\nMissing Items:\n";
            cout << "\n1. Car Keys\n";
            cout << "\n2. House Keys\n";
            cout << "\n3. Cell Phone\n";
            cout << "\nYou have 18 minutes to get to work.\n";
            cout << "\nWhich item will you find first?\n";

            int choice;
            cin >> choice;
            if (choice == 1) {
                cout << "\nSo you've chosen to find your car keys!\n";
                cout << "\nWhere did you last see them?\n";
                cout << "\n...\n";
                cout << "\nThe garage? Ok, well let's head there.\n";
                cout << "\n \n";
                cout << "\nThe Garage\n"
            }
        } else if (choice == 2) {
            cout << "\nSee you later!\n";
            gameRunning = false;
        } else {
            cout << "\nInvalid choice. Try again.\n";
        }
    }

    return 0;
}