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

        while (choice == 1) {
            cout << "\nJuly 31, Thursday, 11:42 am.\n";
            cout << "\nLiving Room\n";
            cout << "\nYou have 18 minutes to get to work.\n";
            cout << "However, you are missing 3 essential items.\n";
            cout << "\nMissing Items:\n";
            cout << "3. Car Keys\n";
            cout << "4. House Keys\n";
            cout << "5. Cell Phone\n";
            cout << "You have 18 minutes to get to work.\n";
            cout << "Which item will you find first?\n";

            int choice;
            cin >> choice;
            if (choice == 3) {
                cout << "\nSo you've chosen to find your car keys!\n";
                cout << "Where did you last see them?\n";
                cout << "\n...\n";
                cout << "The garage? Ok, well let's head there.\n";
                cout << "\n \n";
                cout << "The Garage\n";
                cout << "\n \n";
                cout << "Ok, take a look around! Quickly! You've got to get to work!\n";
                cout << "...i'm hearing an odd sound...\n";
                cout << "\nWhere will you look?\n";
                cout << "1. Under the car\n";
                cout << "2. In boxes\n";
                cout << "3. In the yard supplies\n";
                
                int choice;
                cin >> choice;
                if (choice == 1) {
                    cout << "Did you see anything?\n";
                    cout << "NO? Well keep looking! Time's running out!\n";
                    continue;
                }
                else if (choice == 2) {
                    cout << "Did you see anything?\n";
                    cout << "...a key?? Great! Now you can drive to-\n";
                    cout << "...\n";
                    cout << "It's not your car key? Ok, Is it the house key?\n";
                    cout << "What??? Is it your key at all then???\n";
                    cout << "Ok well, I don't know where it came from, but you have to keep moving. Time's running out and you were already late yesterday!!\n";
                    cout << "1. Pick up the key\n";
                    cout << "2. Leave the key\n";
                }
                else if (choice == 3) {
                    cout << "Did you find anything?\n";
                    cout << "A hole?? Where?\n";
                    cout << "In the floor under the yard supplies? Let me see...\n";
                    cout << "Oh WOW- has that always been there? That's big enough to fit two people inside? Where does it lead? The house is on flat ground, and you don't have a basement...\n";
                    cout << "Anyway, it doesn't matter. You can call an inspector or something as soon as you find your phone. You've gotta keep moving, you're almost late!\n";
                    cout << "1. Jump in the hole\n";
                    cout << "2. Keep looking\n";
                }

            }
            if (choice == 4) {
                cout << "\nSo you've chosen to find your house keys!\n";
                cout << "Where did you last see them?\n";
                cout << "\n...\n";
                cout << "The kitchen counter? Ok, well let's head there.\n";
                cout << "\n \n";
                cout << "The Kitchen\n";
                cout << "\n \n";
                cout << "Ok, take a look around! Quickly! You've got to get to work!\n";
                cout << "...i'm hearing an odd sound...\n";
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