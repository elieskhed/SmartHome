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

    //mise en place du graphique example
    this->createChartsExample();
    this->verticalLayout->addWidget(this->chartView);

    this->setLayout(this->verticalLayout);
}

void MonitorHouseData::createChartsExample(){
    this->series = new QLineSeries;
    // Example
    this->series->append(0, 6);
    this->series->append(2, 4);
    this->series->append(3, 8);
    this->series->append(7, 4);
    this->series->append(10, 5);

    this->chart = new QChart();
    this->chart->legend()->hide();
    this->chart->addSeries(series);
    this->chart->createDefaultAxes();
    this->chart->setTitle("Exemple de Graphique");

    this->chartView = new QChartView(chart);
    this->chartView->setRenderHint(QPainter::Antialiasing);

}
