#include "monitorhousedata.h"

MonitorHouseData::MonitorHouseData() {
    QLabel* labelHouseToken = new QLabel("Token de la maison");
    this->houseToken = new QTextEdit();
    this->houseToken->setFixedSize(750, 50);

    this->buttonSend = new QPushButton("Analyser la donnée");

    this->verticalLayout = new QVBoxLayout();
    this->verticalLayout->addWidget(labelHouseToken);
    this->verticalLayout->addWidget(this->houseToken);
    this->verticalLayout->addWidget(this->buttonSend);

    this->setLayout(this->verticalLayout);

}
