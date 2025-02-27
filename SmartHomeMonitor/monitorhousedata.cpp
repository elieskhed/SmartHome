#include "monitorhousedata.h"

MonitorHouseData::MonitorHouseData() {
    QLabel* labelHouseToken = new QLabel("Token de la maison");
    this->houseToken = new QTextEdit();
    this->houseToken->setFixedSize(750, 50);

    this->checkBoxLastData = new QCheckBox("last data", this);
    this->checkBoxDataFromScratch = new QCheckBox("data from scratch", this);

    this->buttonSend = new QPushButton("Etats du capteur");

    this->verticalLayout = new QVBoxLayout();
    this->verticalLayout->addWidget(labelHouseToken);
    this->verticalLayout->addWidget(this->houseToken);
    this->verticalLayout->addWidget(this->checkBoxLastData);
    this->verticalLayout->addWidget(this->checkBoxDataFromScratch);
    this->verticalLayout->addWidget(this->buttonSend);

    //mise en place du graphique example
    this->createChartsExample();
    this->verticalLayout->addWidget(this->chartView);

    this->setLayout(this->verticalLayout);
}

void MonitorHouseData::createChartsExample(){
    this->series = new QLineSeries;


    this->chart = new QChart();
    this->chart->legend()->hide();
    this->chart->addSeries(series);
    this->chart->createDefaultAxes();
    this->chart->setTitle("Exemple de Graphique");

    this->chartView = new QChartView(chart);
    this->chartView->setRenderHint(QPainter::Antialiasing);

}
