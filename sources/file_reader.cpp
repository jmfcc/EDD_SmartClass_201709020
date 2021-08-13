#include "../headers/file_reader.h"

void readFileStudent(string path_, ListStudent *stud){
    cout<<" >> Path File: "<<path_<<endl;

    string myText; //For lines of the file
    ifstream myFile(path_); // Open the file
    bool init = true;
    string indexHeaders = "";
    // string texto[] = new string[5];
    while(getline(myFile, myText)){
        // cout<<myText<<endl;
        if (init == true){
            init = false;
            indexHeaders = setIndexHeadersStudent(myText, ",");
            // for (int i = 0; i < 8; i++){
            //     cout<< indexHeaders[i] << endl;
            // }
        }else{
            splitTextStudent(myText, ",", indexHeaders, stud);
            // cout << " ------------------------" << endl;
        }
    }

    myFile.close();
    // delete [] indexHeaders;
}

void splitTextStudent(string text_, string pattern_, string indx_, ListStudent *stud){
    size_t pos = 0;
    string token;
    string studentData[8];
    int count = 0;
    while ((pos = text_.find(pattern_)) != string::npos) {
        token = text_.substr(0, pos);
        // cout << token << endl;
        studentData[count] = token;
        text_.erase(0, pos + pattern_.length());
        count++;
    }
    studentData[count] = text_;
    // cout << text_ << endl;
    int listPos[8];
    for (int i = 0; i < 8; i++){
        listPos[i] = indx_[i]-'0';
    }
    stud->insertStudent(std::stoi(studentData[listPos[0]]), studentData[listPos[1]], studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]));
    // students->showListContent();
    // system("pause");
}

string setIndexHeadersStudent(string text_, string pattern_){
    int *iHS_ = new int[8];
    string iHS = "";
    size_t pos = 0;
    string token;
    int index = 0;
    while ((pos = text_.find(pattern_)) != string::npos) {
        token = text_.substr(0, pos);
        int i = getIndexAssignSH(token);
        iHS_[i] = index;
        // cout << token << endl;
        text_.erase(0, pos + pattern_.length());
        index ++;
    }
    // cout << text_ << endl;
    int i = getIndexAssignSH(text_);
    iHS_[i] = index;
    for (int i = 0; i<8; i++){
        iHS += to_string(iHS_[i]);
    }
    return iHS;
}

int getIndexAssignSH(string name_){
    for (int i = 0; i < 8; i++){
        if (name_ == studentFormat[i]){
            return i;
        }
    }
    return -1;
}